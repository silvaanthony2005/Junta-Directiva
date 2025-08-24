"""
Búsqueda Binaria Recursiva
=========================

Teoría:
-------
Divide la lista ordenada y busca recursivamente el objetivo.

Complejidad:
------------
- O(log n)

Uso ideal:
----------
- Listas ordenadas.

Recomendaciones:
----------------
Usar para listas ordenadas y para entender el paradigma divide y vencerás.
"""
def busqueda_binaria_recursiva(arr, objetivo, izquierda, derecha):
    if izquierda > derecha:
        return -1
    medio = (izquierda + derecha) // 2
    if arr[medio] == objetivo:
        return medio
    elif arr[medio] < objetivo:
        return busqueda_binaria_recursiva(arr, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_recursiva(arr, objetivo, izquierda, medio - 1)

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    objetivo = 7
    print(f"Índice de {objetivo}:", busqueda_binaria_recursiva(arr, objetivo, 0, len(arr)-1))
