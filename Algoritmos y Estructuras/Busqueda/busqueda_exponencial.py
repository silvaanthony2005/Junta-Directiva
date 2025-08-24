"""
Búsqueda Exponencial
====================

Teoría:
-------
Encuentra un rango exponencialmente y luego aplica búsqueda binaria.

Complejidad:
------------
- O(log i), donde i es la posición del objetivo.

Requiere orden:
---------------
Sí

Casos de uso ideales:
---------------------
- Listas muy grandes y ordenadas, tamaño desconocido.

Recomendaciones:
----------------
Cuando no se conoce el tamaño exacto de la lista.
"""

def busqueda_binaria(arr, objetivo, izquierda, derecha):
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

def busqueda_exponencial(arr, objetivo):
    if arr[0] == objetivo:
        return 0
    n = len(arr)
    i = 1
    while i < n and arr[i] <= objetivo:
        i *= 2
    return busqueda_binaria(arr, objetivo, i // 2, min(i, n - 1))

if __name__ == "__main__":
    ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    objetivo = 13
    print(f"Índice de {objetivo}:", busqueda_exponencial(ejemplo, objetivo))
