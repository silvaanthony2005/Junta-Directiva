"""
Búsqueda ingenua (Naive)
=======================

Teoría:
-------
Compara el patrón con cada posición posible en el texto.

Complejidad:
------------
- O(n*m)

Uso ideal:
----------
- Textos pequeños o casos simples.

Recomendaciones:
----------------
Usar solo cuando el texto o patrón es pequeño.
"""
def busqueda_ingenua(texto, patron):
    n, m = len(texto), len(patron)
    for i in range(n - m + 1):
        if texto[i:i+m] == patron:
            return i
    return -1

if __name__ == "__main__":
    texto = "abracadabra"
    patron = "cada"
    print(f"Índice de '{patron}':", busqueda_ingenua(texto, patron))
