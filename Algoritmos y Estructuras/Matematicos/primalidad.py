"""
Primalidad básica
================

Teoría:
-------
Prueba si un número es primo comprobando divisores hasta su raíz cuadrada.

Complejidad:
------------
- O(√n)

Uso ideal:
----------
- Primalidad, factorización.

Recomendaciones:
----------------
Usar para comprobar si un número es primo en casos simples.
"""
def es_primo(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    print("¿17 es primo?", es_primo(17))
