"""
Búsqueda en Saltos (Jump Search)
===============================

Teoría:
-------
Salta bloques de tamaño fijo y luego realiza búsqueda lineal en el bloque.

Complejidad:
------------
- O(√n)

Requiere orden:
---------------
Sí

Casos de uso ideales:
---------------------
- Listas ordenadas.

Recomendaciones:
----------------
Alternativa simple a la búsqueda binaria.
"""

import math

def jump_search(arr, objetivo):
    n = len(arr)
    paso = int(math.sqrt(n))
    prev = 0
    while prev < n and arr[min(paso, n) - 1] < objetivo:
        prev = paso
        paso += int(math.sqrt(n))
        if prev >= n:
            return -1
    for i in range(prev, min(paso, n)):
        if arr[i] == objetivo:
            return i
    return -1

if __name__ == "__main__":
    ejemplo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    objetivo = 7
    print(f"Índice de {objetivo}:", jump_search(ejemplo, objetivo))
