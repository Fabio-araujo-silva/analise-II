import csv
from math import inf

# Versão 2: Gera uma tabela com o passo a passo de cada iteração
def secantes_tabela(f, x0, x1, true_root, output_filename="secantes_passos.csv", tol=1e-8, max_iter=100):
    """
    Executa o Método das Secantes e salva os passos em um arquivo CSV.

    Args:
        f (function): A função para a qual se busca a raiz.
        x0 (float): Primeira aproximação inicial.
        x1 (float): Segunda aproximação inicial.
        true_root (float): O valor real da raiz para cálculo do erro.
        output_filename (str): Nome do arquivo CSV de saída.
        tol (float): Tolerância para a convergência.
        max_iter (int): Número máximo de iterações.
    """
    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['k', 'xk', 'f(xk)', 'ek'])

        # Escreve os pontos iniciais k=0 e k=1
        fx0 = f(x0)
        erro0 = abs(x0 - true_root)
        writer.writerow([0, f'{x0:.8f}', f'{fx0:.8f}', f'{erro0:.8f}'])

        fx1 = f(x1)
        erro1 = abs(x1 - true_root)
        writer.writerow([1, f'{x1:.8f}', f'{fx1:.8f}', f'{erro1:.8f}'])

        for k in range(2, max_iter + 2):
            if fx1 - fx0 == 0:
                print("Secantes: Divisão por zero.")
                return {"raiz": None, "iteracoes": k, "convergiu": False}

            x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            fx2 = f(x2)
            erro2 = abs(x2 - true_root)

            writer.writerow([k, f'{x2:.8f}', f'{fx2:.8f}', f'{erro2:.8f}'])

            if abs(x2 - x1) < tol:
                print(f"Secantes: Convergiu em {k} iterações (contando as iniciais).")
                return {"raiz": x2, "iteracoes": k, "convergiu": True}

            x0, x1 = x1, x2
            fx0, fx1 = fx1, fx2

    print("Secantes: Número máximo de iterações atingido.")
    return {"raiz": x1, "iteracoes": max_iter, "convergiu": False}

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # f(x) = x^2 - 4
    def minha_funcao(x):
        return x**2 - 4

    # A raiz verdadeira é 2.0
    raiz_verdadeira = 2.0

    # Parâmetros
    x_inicial_0 = 1.0
    x_inicial_1 = 3.0
    tolerancia = 1e-8

    print("\nExecutando o Método das Secantes e gerando a tabela...")
    resultado = secantes_tabela(minha_funcao, x_inicial_0, x_inicial_1, raiz_verdadeira, tol=tolerancia)

    if resultado["convergiu"]:
        print(f"Raiz encontrada: {resultado['raiz']:.8f}")
    print(f"Tabela de iterações salva em 'secantes_passos.csv'")