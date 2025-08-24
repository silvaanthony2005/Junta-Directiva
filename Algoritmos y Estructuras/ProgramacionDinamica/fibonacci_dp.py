"""
Fibonacci (Programación Dinámica)
================================

Teoría:
-------
Calcula el n-ésimo número de Fibonacci almacenando los resultados previos para evitar cálculos repetidos.

Complejidad:
------------
- O(n)

Uso ideal:
----------
- Secuencias recursivas, optimización de recursión.

Recomendaciones:
----------------
Usar cuando se requiere eficiencia en secuencias recursivas.
"""
def fibonacci_dp(n):
    if n <= 1:
        return n
    fib = [0] * (n + 1)
    fib[1] = 1
    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]
    return fib[n]

if __name__ == "__main__":
    n = 10
    print(f"Fibonacci({n}) =", fibonacci_dp(n))
