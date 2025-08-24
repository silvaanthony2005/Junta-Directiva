"""
Selection Sort
==============

Teoría:
-------
Selection Sort busca el elemento más pequeño en la lista y lo coloca en la primera posición, luego repite el proceso con el resto de la lista.

Complejidad:
------------
- Promedio/Peor caso: O(n²)

Estabilidad:
------------
Inestable (puede cambiar el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Educación, listas pequeñas sin necesidad de estabilidad.

Recomendaciones:
----------------
No recomendado para listas grandes ni cuando la estabilidad es importante.
"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == "__main__":
    ejemplo = [64, 25, 12, 22, 11]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", selection_sort(ejemplo))
