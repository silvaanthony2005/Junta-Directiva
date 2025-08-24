"""
Pila (Stack)
============

Teoría:
-------
Estructura LIFO, operaciones en un solo extremo.

Operaciones principales:
-----------------------
- push, pop, top: O(1)

Uso ideal:
----------
- Algoritmos recursivos, deshacer operaciones.
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else None

    def top(self):
        return self.items[-1] if self.items else None

if __name__ == "__main__":
    pila = Stack()
    pila.push(1)
    pila.push(2)
    print("Elemento en el tope:", pila.top())
    pila.pop()
    print("Elemento en el tope tras pop:", pila.top())
