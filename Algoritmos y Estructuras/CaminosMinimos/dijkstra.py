"""
Dijkstra
========

Teoría:
-------
Encuentra el camino más corto desde un nodo origen a todos los demás en grafos con pesos no negativos. Utiliza una cola de prioridad para seleccionar el nodo más cercano no visitado y actualiza las distancias mínimas a sus vecinos.

Complejidad:
------------
- O((V + E) log V)

Pesos negativos:
----------------
No

Uso ideal:
----------
- Rutas más cortas en mapas, redes, etc.

Recomendaciones:
----------------
Usar cuando todos los pesos son positivos.
"""
import heapq

def dijkstra(grafo, inicio):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[inicio] = 0
    visitado = set()
    heap = [(0, inicio)]
    while heap:
        d, actual = heapq.heappop(heap)
        if actual in visitado:
            continue
        visitado.add(actual)
        for vecino, peso in grafo[actual]:
            if dist[vecino] > d + peso:
                dist[vecino] = d + peso
                heapq.heappush(heap, (dist[vecino], vecino))
    return dist

if __name__ == "__main__":
    grafo = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    inicio = 'A'
    print(f"Distancias mínimas desde {inicio}:", dijkstra(grafo, inicio))
