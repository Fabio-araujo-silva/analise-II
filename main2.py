from bissecao import bissecao
from secantes import secantes
from newton_raphson import newton_raphson as nr

# Função
def f(x):
    return 3*(x**5) + 8*(x**4) - 6*(x**3) - 16*(x**2) - 9*x - 24

# Derivada
def f_prime(x):
    return 15*(x**4) + 32*(x**3) - 18*(x**2) - 32*x - 9

# Newton-Raphson
res_nr = nr(x0=2.0, f=f, f_prime=f_prime, min=-5, max=5)
print("Newton-Raphson:", res_nr)

# Bisseção
res_biss = bissecao(f, a=1, b=2, min=-5, max=5)
print("Bisseção:", res_biss)

# Secantes
res_sec = secantes(f, x0=1, x1=2, min=-5, max=5)
print("Secantes:", res_sec)
