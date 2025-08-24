"""
Insertion Sort
==============

Teoría:
-------
Insertion Sort construye la lista ordenada de izquierda a derecha, insertando cada elemento en su posición correcta dentro de la parte ya ordenada.

Complejidad:
------------
- Promedio/Peor caso: O(n²)
- Mejor caso: O(n) (lista casi ordenada)

Estabilidad:
------------
Estable (no cambia el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Listas pequeñas o casi ordenadas.
- Como parte de algoritmos híbridos (por ejemplo, TimSort).

Recomendaciones:
----------------
Útil para arreglos pequeños o cuando los datos ya están casi ordenados.
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

if __name__ == "__main__":
    ejemplo = [12, 11, 13, 5, 6]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", insertion_sort(ejemplo))
