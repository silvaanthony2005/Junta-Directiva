"""
Exponenciación rápida
====================

Teoría:
-------
Calcula potencias grandes usando divide y vencerás (exponenciación binaria).

Complejidad:
------------
- O(log n)

Uso ideal:
----------
- Criptografía, potencias grandes.

Recomendaciones:
----------------
Usar para cálculos de potencias en números grandes.
"""
def exp_rapida(base, exponente):
    resultado = 1
    while exponente > 0:
        if exponente % 2 == 1:
            resultado *= base
        base *= base
        exponente //= 2
    return resultado

if __name__ == "__main__":
    print("2^10 =", exp_rapida(2, 10))
