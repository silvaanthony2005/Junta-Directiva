"""
Búsqueda Lineal
===============

Teoría:
-------
Recorre la lista elemento por elemento hasta encontrar el objetivo.

Complejidad:
------------
- O(n)

Requiere orden:
---------------
No

Casos de uso ideales:
---------------------
- Listas pequeñas o no ordenadas.

Recomendaciones:
----------------
Útil cuando la lista es pequeña o no está ordenada.
"""

def busqueda_lineal(arr, objetivo):
    for i, elemento in enumerate(arr):
        if elemento == objetivo:
            return i
    return -1

if __name__ == "__main__":
    ejemplo = [3, 5, 2, 4, 9]
    objetivo = 4
    print(f"Índice de {objetivo}:", busqueda_lineal(ejemplo, objetivo))
