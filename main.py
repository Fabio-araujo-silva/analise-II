import numpy as np
import matplotlib.pyplot as plt

from newton_raphson import newton_raphson as nr

# Função
def f(x):
    # 3x^5 + 8x^4 - 6x^3 - 16x^2 - 9x - 24
    return 3*(x**5) + 8*(x**4) - 6*(x**3) - 16*(x**2) - 9*x - 24

# Derivada da função
def f_prime(x):
    # derivada: 15x^4 + 32x^3 - 18x^2 - 32x - 9
    return 15*(x**4) + 32*(x**3) - 18*(x**2) - 32*x - 9

# Exemplo de uso
raiz_1 = nr(x0=-1.5, f = f, f_prime = f_prime, min = -2, max = -1);
print("1 Raiz aproximada:", raiz_1)

raiz_2 = nr(x0=1.5, f = f, f_prime = f_prime, min = 1, max = 2);
print("2 Raiz aproximada:", raiz_2)

# Plot da função
x_vals = np.linspace(-8, 8, 400)

if(raiz_1 is not None):
    y_vals = f(x_vals)

    plt.axhline(0, color='black', linewidth=0.8)
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.scatter(raiz_1, f(raiz_1), color='red', zorder=5, label=f"Raiz ≈ {raiz_1:.4f}")
    plt.ylim(-50, 20)
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Não foi possível encontrar a raiz no intervalo especificado para raiz_1.")

if(raiz_2 is not None):
    y_vals = f(x_vals)

    plt.axhline(0, color='black', linewidth=0.8)
    plt.plot(x_vals, y_vals, label="f(x)")
    plt.scatter(raiz_2, f(raiz_2), color='red', zorder=5, label=f"Raiz ≈ {raiz_2:.4f}")
    plt.ylim(-50, 20)
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("Não foi possível encontrar a raiz no intervalo especificado para raiz_2.")
