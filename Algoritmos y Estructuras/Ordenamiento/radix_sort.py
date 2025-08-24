"""
Radix Sort
==========

Teoría:
-------
Radix Sort ordena los números procesando sus dígitos individualmente, desde el menos significativo al más significativo (LSD) o viceversa (MSD).

Complejidad:
------------
- Promedio/Peor caso: O(nk), donde k es la cantidad de dígitos.

Estabilidad:
------------
Estable (no cambia el orden de elementos iguales).

Casos de uso ideales:
---------------------
- Enteros, cadenas de longitud fija.

Recomendaciones:
----------------
Útil cuando el rango de claves es conocido y pequeño.
"""

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    return arr

if __name__ == "__main__":
    ejemplo = [170, 45, 75, 90, 802, 24, 2, 66]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", radix_sort(ejemplo))
