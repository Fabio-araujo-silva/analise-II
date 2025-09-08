# Autores: Nome Completo do Autor 1, N° USP: 00000000
#          Nome Completo do Autor 2, N° USP: 00000000
#          Nome Completo do Autor 3, N° USP: 00000000

def newton_tabela(f, f_prime, x0, true_root, output_filename="newton_saida.txt", tol=1e-6, max_iter=100):
    """
    Executa o Método de Newton-Raphson e salva os passos em um arquivo de texto formatado.
    """
    xk = x0
    try:
        with open(output_filename, 'w') as file:
            header = f"{'k':<5}{'xk':<20}{'f(xk)':<20}{'f\'(xk)':<20}{'ek':<20}\n"
            file.write(header)
            file.write('-' * len(header) + '\n')

            for k in range(max_iter):
                fxk = f(xk)
                dfxk = f_prime(xk)
                ek = abs(xk - true_root)

                line = f"{k:<5}{xk:<20.8f}{fxk:<20.8f}{dfxk:<20.8f}{ek:<20.8f}\n"
                file.write(line)

                if dfxk == 0:
                    print(f"Newton ({output_filename}): Derivada zero. O método falhou.")
                    return
                
                x_next = xk - fxk / dfxk
                
                # Critério de parada (não usa 'ek')
                if abs(x_next - xk) < tol:
                    print(f"Newton ({output_filename}): Convergiu em {k+1} iterações.")
                    # Escreve o último passo
                    fx_next = f(x_next)
                    dfx_next = f_prime(x_next)
                    ek_next = abs(x_next - true_root)
                    final_line = f"{k+1:<5}{x_next:<20.8f}{fx_next:<20.8f}{dfx_next:<20.8f}{ek_next:<20.8f}\n"
                    file.write(final_line)
                    return
                
                xk = x_next
        
        print(f"Newton ({output_filename}): Atingiu o número máximo de iterações.")

    except IOError:
        print(f"Newton: Erro ao escrever no arquivo {output_filename}.")