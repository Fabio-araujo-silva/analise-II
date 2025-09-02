from math import inf

# Método das Secantes
def secantes(f, x0, x1, tol=1e-6, max_iter=100, min=-inf, max=inf):
    if x0 < min or x1 > max:
        return {"raiz": None, "iteracoes": 0, "convergiu": False, "erro": "Valores iniciais fora dos limites"}

    for n in range(max_iter):
        f0 = f(x0)
        f1 = f(x1)

        if f1 - f0 == 0:
            return {"raiz": None, "iteracoes": n+1, "convergiu": False, "erro": "Divisão por zero"}

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)

        if x2 < min or x2 > max:
            return {"raiz": None, "iteracoes": n+1, "convergiu": False, "erro": "Fora dos limites"}

        if abs(x2 - x1) < tol:
            return {"raiz": x2, "iteracoes": n+1, "convergiu": True}

        x0, x1 = x1, x2

    return {"raiz": x1, "iteracoes": max_iter, "convergiu": False, "erro": "Iterações máximas atingidas"}
