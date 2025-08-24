"""
Búsqueda en Anchura (BFS)
========================

Teoría:
-------
Recorre el grafo por niveles, visitando primero los vecinos más cercanos al nodo inicial. Utiliza una cola para gestionar los nodos a visitar.

Complejidad:
------------
- O(V + E)

Uso ideal:
----------
- Encontrar caminos más cortos en grafos no ponderados.
- Exploración por capas.

Recomendaciones:
----------------
Usar cuando se necesita el camino más corto o explorar por niveles.
"""
from collections import deque

def bfs(grafo, inicio):
    visitado = set()
    cola = deque([inicio])
    recorrido = []
    while cola:
        nodo = cola.popleft()
        if nodo not in visitado:
            visitado.add(nodo)
            recorrido.append(nodo)
            cola.extend([vecino for vecino in grafo[nodo] if vecino not in visitado])
    return recorrido

if __name__ == "__main__":
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    print("Recorrido BFS desde 'A':", bfs(grafo, 'A'))
