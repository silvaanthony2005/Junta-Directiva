"""
Búsqueda Binaria
================

Teoría:
-------
Divide la lista ordenada a la mitad repetidamente para encontrar el objetivo.

Complejidad:
------------
- O(log n)

Requiere orden:
---------------
Sí

Casos de uso ideales:
---------------------
- Listas grandes y ordenadas.

Recomendaciones:
----------------
Usar siempre que la lista esté ordenada.
"""

def busqueda_binaria(arr, objetivo):
    izquierda, derecha = 0, len(arr) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if arr[medio] == objetivo:
            return medio
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    return -1

if __name__ == "__main__":
    ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    objetivo = 6
    print(f"Índice de {objetivo}:", busqueda_binaria(ejemplo, objetivo))
