# Autores: Nome Completo do Autor 1, N° USP: 00000000
#          Nome Completo do Autor 2, N° USP: 00000000
#          Nome Completo do Autor 3, N° USP: 00000000

def bissecao_tabela(f, a, b, true_root, output_filename="bissecao_saida.txt", tol=1e-6, max_iter=100):
    """
    Executa o Método da Bisseção e salva os passos em um arquivo de texto formatado.
    """
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print("Bisseção: Erro - f(a) e f(b) devem ter sinais opostos.")
        return

    try:
        with open(output_filename, 'w') as file:
            # Escreve o cabeçalho formatado
            header = f"{'k':<5}{'a':<20}{'b':<20}{'xk':<20}{'f(xk)':<20}{'ek':<20}\n"
            file.write(header)
            file.write('-' * len(header) + '\n')

            for k in range(max_iter):
                xk = (a + b) / 2
                fxk = f(xk)
                ek = abs(xk - true_root)

                # Escreve os dados da iteração formatados
                line = f"{k:<5}{a:<20.8f}{b:<20.8f}{xk:<20.8f}{fxk:<20.8f}{ek:<20.8f}\n"
                file.write(line)

                # Critério de parada (não usa 'ek')
                if (b - a) / 2 < tol:
                    print(f"Bisseção ({output_filename}): Convergiu em {k+1} iterações.")
                    return

                if fa * fxk < 0:
                    b = xk
                    fb = fxk
                else:
                    a = xk
                    fa = fxk
        
        print(f"Bisseção ({output_filename}): Atingiu o número máximo de iterações.")

    except IOError:
        print(f"Bisseção: Erro ao escrever no arquivo {output_filename}.")