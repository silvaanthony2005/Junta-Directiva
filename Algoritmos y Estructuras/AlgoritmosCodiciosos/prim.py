"""
Árbol de expansión mínimo (Prim)
===============================

Teoría:
-------
Selecciona aristas de menor peso conectando nodos visitados con no visitados.

Complejidad:
------------
- O(E log V)

Uso ideal:
----------
- Redes, grafos conectados.

Recomendaciones:
----------------
Usar cola de prioridad para eficiencia.
"""
import heapq

def prim(grafo):
    V = len(grafo)
    visitado = [False] * V
    min_heap = [(0, 0)]  # (peso, nodo)
    total = 0
    while min_heap:
        peso, u = heapq.heappop(min_heap)
        if visitado[u]:
            continue
        visitado[u] = True
        total += peso
        for v, w in grafo[u]:
            if not visitado[v]:
                heapq.heappush(min_heap, (w, v))
    return total

if __name__ == "__main__":
    grafo = {
        0: [(1, 2), (3, 6)],
        1: [(0, 2), (2, 3), (3, 8), (4, 5)],
        2: [(1, 3), (4, 7)],
        3: [(0, 6), (1, 8), (4, 9)],
        4: [(1, 5), (2, 7), (3, 9)]
    }
    print("Peso total del árbol de expansión mínimo:", prim(grafo))
