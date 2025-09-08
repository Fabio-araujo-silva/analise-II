# Autores: FABIO KAUÊ ARAUJO DA SILVA, N° USP: 16311045
#          PEDRO ANHIEVISK, N° USP: 15656521 

import math
from bissecao import bissecao_tabela
from newton_raphson import newton_tabela
from secantes import secantes_tabela

# --- Definição da Função e sua Derivada ---
def f(x):
    """Função polinomial do problema."""
    return 3*x**5 + 8*x**4 - 6*x**3 - 16*x**2 - 9*x - 24

def f_prime(x):
    """Derivada da função polinomial."""
    return 15*x**4 + 32*x**3 - 18*x**2 - 32*x - 9

# --- Raízes Exatas (para cálculo do erro na tabela) ---
# Raiz no intervalo [-2, -1]
raiz_exata_1 = (-1 - math.sqrt(5)) / 2
# Raiz no intervalo [1, 2]
raiz_exata_2 = math.sqrt(3)

# --- Parâmetros Comuns ---
TOLERANCIA = 1e-6
MAX_ITER = 100

print("Iniciando a execução dos métodos numéricos...")

# --- Execução para a Raiz 1 (Intervalo [-2, -1]) ---
print("\n--- Calculando a raiz no intervalo [-2, -1] ---")
bissecao_tabela(f, a=-2.0, b=-1.0, true_root=raiz_exata_1, output_filename="bissecao_saida1.txt", tol=TOLERANCIA, max_iter=MAX_ITER)
newton_tabela(f, f_prime, x0=-1.5, true_root=raiz_exata_1, output_filename="newton_saida1.txt", tol=TOLERANCIA, max_iter=MAX_ITER)
secantes_tabela(f, x0=-2.0, x1=-1.0, true_root=raiz_exata_1, output_filename="secantes_saida1.txt", tol=TOLERANCIA, max_iter=MAX_ITER)

# --- Execução para a Raiz 2 (Intervalo [1, 2]) ---
print("\n--- Calculando a raiz no intervalo [1, 2] ---")
bissecao_tabela(f, a=1.0, b=2.0, true_root=raiz_exata_2, output_filename="bissecao_saida2.txt", tol=TOLERANCIA, max_iter=MAX_ITER)
newton_tabela(f, f_prime, x0=2.0, true_root=raiz_exata_2, output_filename="newton_saida2.txt", tol=TOLERANCIA, max_iter=MAX_ITER)
secantes_tabela(f, x0=1.0, x1=2.0, true_root=raiz_exata_2, output_filename="secantes_saida2.txt", tol=TOLERANCIA, max_iter=MAX_ITER)

print("\nExecução concluída. Arquivos de saída foram gerados.")