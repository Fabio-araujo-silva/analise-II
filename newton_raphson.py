import csv
from math import inf

# Versão 2: Gera uma tabela com o passo a passo de cada iteração
def newton_raphson_tabela(f, f_prime, x0, true_root, output_filename="newton_passos.csv", tol=1e-8, max_iter=100):
    """
    Executa o Método de Newton-Raphson e salva os passos em um arquivo CSV.

    Args:
        f (function): A função para a qual se busca a raiz.
        f_prime (function): A derivada da função f.
        x0 (float): A aproximação inicial.
        true_root (float): O valor real da raiz para cálculo do erro.
        output_filename (str): Nome do arquivo CSV de saída.
        tol (float): Tolerância para a convergência.
        max_iter (int): Número máximo de iterações.
    """
    xn = x0

    with open(output_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['k', 'xk', 'f(xk)', "f'(xk)", 'ek'])

        for k in range(max_iter):
            fxn = f(xn)
            dfxn = f_prime(xn)
            erro = abs(xn - true_root)

            # Escreve os dados da iteração atual
            writer.writerow([
                k,
                f'{xn:.8f}',
                f'{fxn:.8f}',
                f'{dfxn:.8f}',
                f'{erro:.8f}'
            ])

            if dfxn == 0:
                print("Newton: Derivada zero. O método falhou.")
                return {"raiz": None, "iteracoes": k, "convergiu": False}
            
            x_next = xn - fxn / dfxn
            
            if abs(x_next - xn) < tol:
                print(f"Newton: Convergiu em {k+1} iterações.")
                # Escreve o último passo antes de retornar
                fx_next = f(x_next)
                dfx_next = f_prime(x_next)
                erro_next = abs(x_next - true_root)
                writer.writerow([k+1, f'{x_next:.8f}', f'{fx_next:.8f}', f'{dfx_next:.8f}', f'{erro_next:.8f}'])
                return {"raiz": x_next, "iteracoes": k+1, "convergiu": True}
            
            xn = x_next
    
    print("Newton: Número máximo de iterações atingido.")
    return {"raiz": xn, "iteracoes": max_iter, "convergiu": False}

# --- Exemplo de Uso ---
if __name__ == "__main__":
    # f(x) = x^2 - 4
    def minha_funcao(x):
        return x**2 - 4

    # f'(x) = 2x
    def minha_funcao_derivada(x):
        return 2 * x

    # A raiz verdadeira é 2.0
    raiz_verdadeira = 2.0

    # Parâmetros
    chute_inicial = 3.0
    tolerancia = 1e-8

    print("\nExecutando o Método de Newton-Raphson e gerando a tabela...")
    resultado = newton_raphson_tabela(minha_funcao, minha_funcao_derivada, chute_inicial, raiz_verdadeira, tol=tolerancia)

    if resultado["convergiu"]:
        print(f"Raiz encontrada: {resultado['raiz']:.8f}")
    print(f"Tabela de iterações salva em 'newton_passos.csv'")