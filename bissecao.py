import csv
from math import inf

# Função original para referência (não modificada)
def bissecao(f, a, b, tol=1e-6, max_iter=100, min=-inf, max=inf):
    # ... (código original) ...
    pass

# Versão 2: Gera uma tabela com o passo a passo de cada iteração
def bissecao_tabela(f, a, b, true_root, output_filename="bissecao_passos.csv", tol=1e-8, max_iter=100):
    """
    Executa o Método da Bisseção e salva os passos em um arquivo CSV.

    Args:
        f (function): A função para a qual se busca a raiz.
        a (float): Início do intervalo.
        b (float): Fim do intervalo.
        true_root (float): O valor real da raiz para cálculo do erro.
        output_filename (str): Nome do arquivo CSV de saída.
        tol (float): Tolerância para a convergência.
        max_iter (int): Número máximo de iterações.
    """
    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        print("Erro: f(a) e f(b) devem ter sinais opostos.")
        return {"raiz": None, "iteracoes": 0, "convergiu": False}

    # Abre o arquivo para escrita e define o cabeçalho
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['k', 'a', 'b', 'xk', 'f(xk)', 'ek'])

        for k in range(max_iter):
            m = (a + b) / 2
            fm = f(m)
            erro = abs(m - true_root)

            # Escreve os dados da iteração atual no arquivo
            # Formata para garantir pelo menos 8 casas decimais
            writer.writerow([
                k,
                f'{a:.8f}',
                f'{b:.8f}',
                f'{m:.8f}',
                f'{fm:.8f}',
                f'{erro:.8f}'
            ])

            if abs(fm) < tol or (b - a) / 2 < tol:
                print(f"Bisseção: Convergiu em {k+1} iterações.")
                return {"raiz": m, "iteracoes": k+1, "convergiu": True}

            if fa * fm < 0:
                b = m
                fb = fm
            else:
                a = m
                fa = fm

    print("Bisseção: Número máximo de iterações atingido.")
    return {"raiz": (a + b) / 2, "iteracoes": max_iter, "convergiu": False}

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # Definindo a função para encontrar a raiz, por exemplo: f(x) = x^2 - 4
    def minha_funcao(x):
        return x**2 - 4

    # A raiz verdadeira de x^2 - 4 = 0 no intervalo [1, 3] é 2.
    raiz_verdadeira = 2.0

    # Parâmetros
    intervalo_a = 1.0
    intervalo_b = 3.0
    tolerancia = 1e-8

    print("Executando o Método da Bisseção e gerando a tabela...")
    resultado = bissecao_tabela(minha_funcao, intervalo_a, intervalo_b, raiz_verdadeira, tol=tolerancia)
    
    if resultado["convergiu"]:
        print(f"Raiz encontrada: {resultado['raiz']:.8f}")
    print(f"Tabela de iterações salva em 'bissecao_passos.csv'")