# Autores: Nome Completo do Autor 1, N° USP: 00000000
#          Nome Completo do Autor 2, N° USP: 00000000
#          Nome Completo do Autor 3, N° USP: 00000000

def secantes_tabela(f, x0, x1, true_root, output_filename="secantes_saida.txt", tol=1e-6, max_iter=100):
    """
    Executa o Método das Secantes e salva os passos em um arquivo de texto formatado.
    """
    fx0 = f(x0)
    fx1 = f(x1)

    try:
        with open(output_filename, 'w') as file:
            header = f"{'k':<5}{'xk':<20}{'f(xk)':<20}{'ek':<20}\n"
            file.write(header)
            file.write('-' * len(header) + '\n')

            # Escreve os pontos iniciais k=0 e k=1
            ek0 = abs(x0 - true_root)
            file.write(f"{0:<5}{x0:<20.8f}{fx0:<20.8f}{ek0:<20.8f}\n")
            ek1 = abs(x1 - true_root)
            file.write(f"{1:<5}{x1:<20.8f}{fx1:<20.8f}{ek1:<20.8f}\n")

            for k in range(2, max_iter + 2):
                if fx1 - fx0 == 0:
                    print(f"Secantes ({output_filename}): Divisão por zero. O método falhou.")
                    return

                xk_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
                fxk_next = f(xk_next)
                ek_next = abs(xk_next - true_root)

                file.write(f"{k:<5}{xk_next:<20.8f}{fxk_next:<20.8f}{ek_next:<20.8f}\n")

                # Critério de parada (não usa 'ek')
                if abs(xk_next - x1) < tol:
                    print(f"Secantes ({output_filename}): Convergiu em {k} iterações.")
                    return

                x0, x1 = x1, xk_next
                fx0, fx1 = fx1, fxk_next

        print(f"Secantes ({output_filename}): Atingiu o número máximo de iterações.")

    except IOError:
        print(f"Secantes: Erro ao escrever no arquivo {output_filename}.")