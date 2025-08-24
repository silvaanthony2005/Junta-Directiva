"""
Bellman-Ford
============

Teoría:
-------
Permite encontrar caminos más cortos incluso con pesos negativos y detecta ciclos negativos. Relaja todas las aristas repetidamente.

Complejidad:
------------
- O(V * E)

Pesos negativos:
----------------
Sí

Uso ideal:
----------
- Cuando hay posibilidad de pesos negativos.

Recomendaciones:
----------------
Usar si existen aristas con peso negativo o se requiere detectar ciclos negativos.
"""
def bellman_ford(grafo, V, inicio):
    dist = {v: float('inf') for v in range(V)}
    dist[inicio] = 0
    for _ in range(V - 1):
        for u in grafo:
            for v, peso in grafo[u]:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
    # Detección de ciclos negativos
    for u in grafo:
        for v, peso in grafo[u]:
            if dist[u] + peso < dist[v]:
                return "Ciclo negativo detectado"
    return dist

if __name__ == "__main__":
    # Grafo como lista de adyacencia con índices numéricos
    grafo = {
        0: [(1, -1), (2, 4)],
        1: [(2, 3), (3, 2), (4, 2)],
        2: [],
        3: [(1, 1), (2, 5)],
        4: [(3, -3)]
    }
    V = 5
    inicio = 0
    print(f"Distancias mínimas desde {inicio}:", bellman_ford(grafo, V, inicio))
