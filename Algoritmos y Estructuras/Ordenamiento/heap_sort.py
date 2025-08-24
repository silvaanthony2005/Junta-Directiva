"""
Heap Sort
=========

Teoría:
-------
Heap Sort convierte la lista en un heap (montículo) y extrae el elemento máximo repetidamente para construir la lista ordenada.

Complejidad:
------------
- Promedio/Peor caso: O(n log n)

Estabilidad:
------------
Inestable (puede cambiar el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Sistemas embebidos.
- Cuando no se puede usar memoria adicional.

Recomendaciones:
----------------
Útil cuando la eficiencia es importante y la memoria adicional es limitada.
"""

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
    return arr

if __name__ == "__main__":
    ejemplo = [12, 11, 13, 5, 6, 7]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", heap_sort(ejemplo))
