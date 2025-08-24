"""
Factorial Recursivo
==================

Teoría:
-------
Calcula el producto de todos los enteros positivos hasta n usando recursión.

Complejidad:
------------
- O(n)

Uso ideal:
----------
- Matemáticas, combinatoria.

Recomendaciones:
----------------
Usar para valores pequeños o demostraciones de recursión.
"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print("Factorial de 5:", factorial(5))
