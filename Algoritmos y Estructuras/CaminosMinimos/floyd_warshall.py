"""
Floyd-Warshall
==============

Teoría:
-------
Calcula los caminos más cortos entre todos los pares de nodos usando programación dinámica.

Complejidad:
------------
- O(V³)

Pesos negativos:
----------------
Sí

Uso ideal:
----------
- Grafos densos, todos los pares de caminos más cortos.

Recomendaciones:
----------------
Usar para grafos pequeños o medianos donde se requiere conocer todos los caminos mínimos.
"""
def floyd_warshall(grafo):
    V = len(grafo)
    dist = [[float('inf')] * V for _ in range(V)]
    for u in range(V):
        dist[u][u] = 0
        for v, peso in grafo[u]:
            dist[u][v] = peso
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist

if __name__ == "__main__":
    # Grafo como lista de adyacencia con índices numéricos
    grafo = {
        0: [(1, 3), (2, 8), (4, -4)],
        1: [(3, 1), (4, 7)],
        2: [(1, 4)],
        3: [(0, 2), (2, -5)],
        4: [(3, 6)]
    }
    resultado = floyd_warshall(grafo)
    print("Matriz de distancias mínimas:")
    for fila in resultado:
        print(fila)
