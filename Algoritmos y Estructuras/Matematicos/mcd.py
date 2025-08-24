"""
Máximo común divisor (MCD)
=========================

Teoría:
-------
Algoritmo de Euclides para encontrar el mayor divisor común de dos números.

Complejidad:
------------
- O(log n)

Uso ideal:
----------
- Simplificación de fracciones, aritmética modular.

Recomendaciones:
----------------
Usar para simplificar fracciones y problemas de divisibilidad.
"""
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    print("MCD de 48 y 18:", mcd(48, 18))
