from math import inf

# Método da Bisseção
def bissecao(f, a, b, tol=1e-6, max_iter=100, min=-inf, max=inf):
    if a < min or b > max:
        return {"raiz": None, "iteracoes": 0, "convergiu": False, "erro": "Intervalo fora dos limites"}

    fa = f(a)
    fb = f(b)

    if fa * fb > 0:
        return {"raiz": None, "iteracoes": 0, "convergiu": False, "erro": "f(a) e f(b) têm o mesmo sinal"}

    for n in range(max_iter):
        m = (a + b) / 2
        fm = f(m)

        if m < min or m > max:
            return {"raiz": None, "iteracoes": n+1, "convergiu": False, "erro": "Fora dos limites"}

        if abs(fm) < tol or (b - a) / 2 < tol:
            return {"raiz": m, "iteracoes": n+1, "convergiu": True}

        if fa * fm < 0:
            b = m
            fb = fm
        else:
            a = m
            fa = fm

    return {"raiz": (a + b) / 2, "iteracoes": max_iter, "convergiu": False, "erro": "Iterações máximas atingidas"}
