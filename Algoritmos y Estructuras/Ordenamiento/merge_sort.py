"""
Merge Sort
==========

Teoría:
-------
Merge Sort es un algoritmo de divide y vencerás. Divide la lista en mitades, ordena cada mitad y luego las fusiona en una lista ordenada.

Complejidad:
------------
- Promedio/Peor caso: O(n log n)

Estabilidad:
------------
Estable (no cambia el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Grandes volúmenes de datos.
- Ordenamiento externo (archivos grandes).

Recomendaciones:
----------------
Recomendado cuando se necesita estabilidad y se trabaja con estructuras grandes.
"""

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

if __name__ == "__main__":
    ejemplo = [12, 11, 13, 5, 6, 7]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", merge_sort(ejemplo))
