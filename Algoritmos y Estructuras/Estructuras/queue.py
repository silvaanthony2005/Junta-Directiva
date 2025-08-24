"""
Cola (Queue)
============

Teoría:
-------
Estructura FIFO, operaciones en extremos opuestos.

Operaciones principales:
-----------------------
- enqueue, dequeue, front: O(1)

Uso ideal:
----------
- Procesamiento por turnos, algoritmos BFS.
"""
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0) if self.items else None

    def front(self):
        return self.items[0] if self.items else None

if __name__ == "__main__":
    cola = Queue()
    cola.enqueue(1)
    cola.enqueue(2)
    print("Elemento al frente:", cola.front())
    cola.dequeue()
    print("Elemento al frente tras dequeue:", cola.front())
