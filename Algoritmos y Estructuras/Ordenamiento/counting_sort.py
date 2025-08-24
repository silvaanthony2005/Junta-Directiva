"""
Counting Sort
=============

Teoría:
-------
Counting Sort cuenta la cantidad de ocurrencias de cada valor y utiliza esa información para posicionar los elementos en la lista ordenada.

Complejidad:
------------
- Promedio/Peor caso: O(n + k), donde k es el rango de los datos.

Estabilidad:
------------
Estable (no cambia el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Enteros en rango pequeño.

Recomendaciones:
----------------
Útil cuando el rango de valores es limitado y los datos son enteros.
"""

def counting_sort(arr):
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    count = [0] * range_of_elements
    output = [0] * len(arr)
    for i in range(len(arr)):
        count[arr[i] - min_val] += 1
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    for i in range(len(arr) - 1, -1, -1):
        output[count[arr[i] - min_val] - 1] = arr[i]
        count[arr[i] - min_val] -= 1
    for i in range(len(arr)):
        arr[i] = output[i]
    return arr

if __name__ == "__main__":
    ejemplo = [4, 2, 2, 8, 3, 3, 1]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", counting_sort(ejemplo))
