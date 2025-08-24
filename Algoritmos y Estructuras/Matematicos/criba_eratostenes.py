"""
Criba de Eratóstenes
===================

Teoría:
-------
Genera todos los números primos hasta n de forma eficiente.

Complejidad:
------------
- O(n log log n)

Uso ideal:
----------
- Listas de primos, criptografía.

Recomendaciones:
----------------
Usar para generar listas de primos grandes.
"""
def criba_eratostenes(n):
    primos = [True] * (n + 1)
    primos[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if primos[i]:
            for j in range(i*i, n+1, i):
                primos[j] = False
    return [i for i, es_primo in enumerate(primos) if es_primo]

if __name__ == "__main__":
    print("Primos hasta 30:", criba_eratostenes(30))
