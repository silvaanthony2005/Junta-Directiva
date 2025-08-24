"""
Árbol binario (Binary Tree)
==========================

Teoría:
-------
Cada nodo tiene hasta dos hijos, estructura jerárquica.

Operaciones principales:
-----------------------
- Inserción, búsqueda, recorrido: O(log n) promedio

Uso ideal:
----------
- Búsqueda, jerarquías, ordenamientos.
"""
class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if not self.raiz:
            self.raiz = NodoArbol(valor)
        else:
            self._insertar(self.raiz, valor)

    def _insertar(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izq:
                self._insertar(nodo.izq, valor)
            else:
                nodo.izq = NodoArbol(valor)
        else:
            if nodo.der:
                self._insertar(nodo.der, valor)
            else:
                nodo.der = NodoArbol(valor)

    def inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if nodo:
            self.inorden(nodo.izq)
            print(nodo.valor, end=" ")
            self.inorden(nodo.der)

if __name__ == "__main__":
    arbol = ArbolBinario()
    arbol.insertar(5)
    arbol.insertar(3)
    arbol.insertar(7)
    print("Recorrido inorden:", end=" ")
    arbol.inorden()
    print()
