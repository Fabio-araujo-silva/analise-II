# Autores: FABIO KAUÊ ARAUJO DA SILVA, N° USP: 16311045
#          PEDRO ANHIEVISK, N° USP: 15656521 

from arredondamento import arredondar_especial

def newton_tabela(f, f_prime, x0, true_root, output_filename="newton_saida.txt", tol=1e-6, max_iter=100):
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

                # Arredonda os valores
                xk_r = arredondar_especial(xk, 8)
                fxk_r = arredondar_especial(fxk, 8)
                dfxk_r = arredondar_especial(dfxk, 8)
                ek_r = arredondar_especial(ek, 8)

                line = f"{k:<5}{xk_r:<20.8f}{fxk_r:<20.8f}{dfxk_r:<20.8f}{ek_r:<20.8f}\n"
                file.write(line)

                if dfxk == 0:
                    print(f"Newton ({output_filename}): Derivada zero. O método falhou.")
                    return
                
                x_next = xk - fxk / dfxk
                
                if abs(x_next - xk) < tol:
                    print(f"Newton ({output_filename}): Convergiu em {k+1} iterações.")
                    fx_next = f(x_next)
                    dfx_next = f_prime(x_next)
                    ek_next = abs(x_next - true_root)
                    
                    # Arredonda o último passo
                    x_next_r = arredondar_especial(x_next, 8)
                    fx_next_r = arredondar_especial(fx_next, 8)
                    dfx_next_r = arredondar_especial(dfx_next, 8)
                    ek_next_r = arredondar_especial(ek_next, 8)
                    
                    final_line = f"{k+1:<5}{x_next_r:<20.8f}{fx_next_r:<20.8f}{dfx_next_r:<20.8f}{ek_next_r:<20.8f}\n"
                    file.write(final_line)
                    return
                
                xk = x_next
        
        print(f"Newton ({output_filename}): Atingiu o número máximo de iterações.")

    except IOError:
        print(f"Newton: Erro ao escrever no arquivo {output_filename}.")