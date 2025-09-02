from math import inf

def f(x):
    return x if x > 0 else -x

def f_line(x):
    return 1 if x > 0 else -1

# Método de Newton-Raphson
def newton_raphson(x0, tol = 1e-6, max_iter = 100, f = f, f_prime = f_line, min = -inf, max = inf):
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        dfxn = f_prime(xn)
        
        if dfxn == 0:
            print("Derivada zero. O método falhou.")
            return None
        
        x_next = xn - fxn/dfxn
        if(x_next < min or x_next > max):
            print("A próxima aproximação está fora dos limites especificados.")
            return None
        
        if abs(x_next - xn) < tol:
            print(f"Convergiu em {n+1} iterações.")
            return x_next
        
        xn = x_next
    
    print("Número máximo de iterações atingido.")
    return xn
