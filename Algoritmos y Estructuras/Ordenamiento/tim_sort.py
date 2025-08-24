"""
Tim Sort
========

Teoría:
-------
Tim Sort es un algoritmo híbrido que combina Insertion Sort y Merge Sort. Es el algoritmo de ordenación por defecto en Python y Java.

Complejidad:
------------
- Promedio/Peor caso: O(n log n)

Estabilidad:
------------
Estable (no cambia el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Ordenamiento general en Python y Java.
- Datos parcialmente ordenados.

Recomendaciones:
----------------
Ideal para uso general: rápido, estable y adaptativo.
"""

# Nota: Python ya implementa TimSort en sorted() y list.sort().
def tim_sort(arr):
    return sorted(arr)

if __name__ == "__main__":
    ejemplo = [5, 21, 7, 23, 19]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", tim_sort(ejemplo))
