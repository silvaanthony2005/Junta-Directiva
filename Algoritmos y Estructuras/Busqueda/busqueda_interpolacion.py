"""
Búsqueda por Interpolación
==========================

Teoría:
-------
Estima la posición probable del objetivo usando interpolación.

Complejidad:
------------
- Mejor caso: O(log log n)
- Peor caso: O(n)

Requiere orden:
---------------
Sí (y distribución uniforme)

Casos de uso ideales:
---------------------
- Listas ordenadas y distribuidas uniformemente.

Recomendaciones:
----------------
Cuando los datos son numéricos y uniformes.
"""

def busqueda_interpolacion(arr, objetivo):
    bajo = 0
    alto = len(arr) - 1
    while bajo <= alto and objetivo >= arr[bajo] and objetivo <= arr[alto]:
        if bajo == alto:
            if arr[bajo] == objetivo:
                return bajo
            return -1
        pos = bajo + ((alto - bajo) * (objetivo - arr[bajo])) // (arr[alto] - arr[bajo])
        if arr[pos] == objetivo:
            return pos
        if arr[pos] < objetivo:
            bajo = pos + 1
        else:
            alto = pos - 1
    return -1

if __name__ == "__main__":
    ejemplo = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    objetivo = 70
    print(f"Índice de {objetivo}:", busqueda_interpolacion(ejemplo, objetivo))
