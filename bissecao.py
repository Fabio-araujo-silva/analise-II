# Autores: FABIO KAUÊ ARAUJO DA SILVA, N° USP: 16311045
#          PEDRO ANHIEVISK, N° USP: 00000000

from arredondamento import arredondar_especial

def bissecao_tabela(f, a, b, true_root, output_filename="bissecao_saida.txt", tol=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)

    if fa * fb >= 0:
        print("Bisseção: Erro - f(a) e f(b) devem ter sinais opostos.")
        return

    try:
        with open(output_filename, 'w') as file:
            header = f"{'k':<5}{'a':<20}{'b':<20}{'xk':<20}{'f(xk)':<20}{'ek':<20}\n"
            file.write(header)
            file.write('-' * len(header) + '\n')

            for k in range(max_iter):
                xk = (a + b) / 2
                fxk = f(xk)
                ek = abs(xk - true_root)

                # Arredonda os valores antes de escrever no arquivo
                a_r = arredondar_especial(a, 8)
                b_r = arredondar_especial(b, 8)
                xk_r = arredondar_especial(xk, 8)
                fxk_r = arredondar_especial(fxk, 8)
                ek_r = arredondar_especial(ek, 8)

                line = f"{k:<5}{a_r:<20.8f}{b_r:<20.8f}{xk_r:<20.8f}{fxk_r:<20.8f}{ek_r:<20.8f}\n"
                file.write(line)

                if (b - a) / 2 < tol:
                    print(f"Bisseção ({output_filename}): Convergiu em {k+1} iterações.")
                    return

                if fa * fxk < 0:
                    b = xk
                else:
                    a = xk
                    fa = fxk
        
        print(f"Bisseção ({output_filename}): Atingiu o número máximo de iterações.")

    except IOError:
        print(f"Bisseção: Erro ao escrever no arquivo {output_filename}.")