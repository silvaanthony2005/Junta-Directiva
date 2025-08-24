"""
Lista enlazada (Linked List)
===========================

Teoría:
-------
Nodos conectados entre sí, tamaño dinámico.

Operaciones principales:
-----------------------
- Inserción/borrado al inicio: O(1)
- Búsqueda: O(n)

Uso ideal:
----------
- Inserciones/borrados frecuentes, tamaño variable.
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def mostrar(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

if __name__ == "__main__":
    lista = ListaEnlazada()
    lista.insertar_inicio(3)
    lista.insertar_inicio(2)
    lista.insertar_inicio(1)
    lista.mostrar()
