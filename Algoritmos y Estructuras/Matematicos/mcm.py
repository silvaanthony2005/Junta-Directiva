"""
Mínimo común múltiplo (MCM)
==========================

Teoría:
-------
Calcula el menor múltiplo común usando el MCD.

Complejidad:
------------
- O(log n)

Uso ideal:
----------
- Operaciones con fracciones.

Recomendaciones:
----------------
Usar junto con el MCD para operaciones con fracciones.
"""
def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

if __name__ == "__main__":
    print("MCM de 12 y 18:", mcm(12, 18))
