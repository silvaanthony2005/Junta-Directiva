"""
Bubble Sort
===========

Teoría:
-------
Bubble Sort es un algoritmo sencillo que compara elementos adyacentes e intercambia sus posiciones si están en el orden incorrecto. Este proceso se repite hasta que la lista está ordenada.

Complejidad:
------------
- Promedio/Peor caso: O(n²)
- Mejor caso: O(n) (cuando la lista ya está ordenada)

Estabilidad:
------------
Estable (no cambia el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Educación y visualización de conceptos básicos de ordenación.
- Listas muy pequeñas.

Recomendaciones:
----------------
No se recomienda para producción ni listas grandes. Útil solo para enseñanza.
"""

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    ejemplo = [64, 34, 25, 12, 22, 11, 90]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", bubble_sort(ejemplo))
