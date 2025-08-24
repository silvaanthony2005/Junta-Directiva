"""
Torres de Hanoi
===============

Teoría:
-------
Mueve n discos de una torre a otra siguiendo reglas específicas usando recursión múltiple.

Complejidad:
------------
- O(2^n)

Uso ideal:
----------
- Problemas de movimiento, recursión múltiple.

Recomendaciones:
----------------
Usar para entender recursión y descomposición de problemas.
"""
def torres_de_hanoi(n, origen, destino, auxiliar, movimientos=None):
    if movimientos is None:
        movimientos = []
    if n == 1:
        movimientos.append((origen, destino))
    else:
        torres_de_hanoi(n-1, origen, auxiliar, destino, movimientos)
        movimientos.append((origen, destino))
        torres_de_hanoi(n-1, auxiliar, destino, origen, movimientos)
    return movimientos

if __name__ == "__main__":
    movimientos = torres_de_hanoi(3, 'A', 'C', 'B')
    print("Movimientos para 3 discos:")
    for mov in movimientos:
        print(f"Mover de {mov[0]} a {mov[1]}")
