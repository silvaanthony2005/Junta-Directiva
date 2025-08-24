"""
Fibonacci Recursivo
==================

Teoría:
-------
Suma los dos anteriores para obtener el siguiente número de la secuencia.

Complejidad:
------------
- O(2^n)

Uso ideal:
----------
- Demostración de recursión, no para grandes n.

Recomendaciones:
----------------
No usar para valores grandes, preferir DP para eficiencia.
"""
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    print("Fibonacci(6):", fibonacci(6))
