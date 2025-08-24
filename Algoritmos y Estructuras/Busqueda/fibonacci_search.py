"""
Búsqueda Fibonacci
==================

Teoría:
-------
Utiliza números de Fibonacci para dividir la lista y buscar el objetivo.

Complejidad:
------------
- O(log n)

Requiere orden:
---------------
Sí

Casos de uso ideales:
---------------------
- Listas ordenadas, hardware con acceso secuencial.

Recomendaciones:
----------------
Útil en sistemas donde la búsqueda binaria no es eficiente.
"""

def fibonacci_search(arr, objetivo):
    n = len(arr)
    fibMMm2 = 0
    fibMMm1 = 1
    fibM = fibMMm2 + fibMMm1
    while fibM < n:
        fibMMm2 = fibMMm1
        fibMMm1 = fibM
        fibM = fibMMm2 + fibMMm1
    offset = -1
    while fibM > 1:
        i = min(offset + fibMMm2, n - 1)
        if arr[i] < objetivo:
            fibM = fibMMm1
            fibMMm1 = fibMMm2
            fibMMm2 = fibM - fibMMm1
            offset = i
        elif arr[i] > objetivo:
            fibM = fibMMm2
            fibMMm1 = fibMMm1 - fibMMm2
            fibMMm2 = fibM - fibMMm1
        else:
            return i
    if fibMMm1 and offset + 1 < n and arr[offset + 1] == objetivo:
        return offset + 1
    return -1

if __name__ == "__main__":
    ejemplo = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
    objetivo = 85
    print(f"Índice de {objetivo}:", fibonacci_search(ejemplo, objetivo))
