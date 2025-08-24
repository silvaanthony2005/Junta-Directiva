"""
Quick Sort
==========

Teoría:
-------
Quick Sort es un algoritmo de divide y vencerás. Selecciona un pivote, particiona la lista en elementos menores y mayores al pivote, y ordena recursivamente cada parte.

Complejidad:
------------
- Promedio: O(n log n)
- Peor caso: O(n²)

Estabilidad:
------------
Inestable (puede cambiar el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Listas grandes en memoria.

Recomendaciones:
----------------
Muy rápido en la práctica, pero no es estable. No recomendado si se requiere estabilidad.
"""

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    ejemplo = [10, 7, 8, 9, 1, 5]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", quick_sort(ejemplo))
