"""
Lista (Array)
=============

Teoría:
-------
Estructura secuencial de tamaño fijo, acceso rápido por índice.

Operaciones principales:
-----------------------
- Acceso: O(1)
- Inserción/borrado: O(n)

Uso ideal:
----------
- Cuando se conoce el tamaño y se requiere acceso rápido.
"""
class Array:
    def __init__(self, size):
        self.data = [None] * size
        self.size = size

    def set(self, index, value):
        self.data[index] = value

    def get(self, index):
        return self.data[index]

if __name__ == "__main__":
    arr = Array(5)
    arr.set(0, 10)
    arr.set(1, 20)
    print("Elemento en posición 1:", arr.get(1))
