"""
Árbol de expansión mínimo (Kruskal)
===================================

Teoría:
-------
Selecciona aristas de menor peso que no formen ciclos hasta conectar todos los nodos.

Complejidad:
------------
- O(E log V)

Uso ideal:
----------
- Redes, grafos conectados.

Recomendaciones:
----------------
Usar estructuras de conjuntos disjuntos (Union-Find).
"""
def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskal(V, aristas):
    resultado = []
    aristas = sorted(aristas, key=lambda x: x[2])
    parent = [i for i in range(V)]
    rank = [0] * V
    e = 0
    i = 0
    while e < V - 1:
        u, v, w = aristas[i]
        i += 1
        x = find(parent, u)
        y = find(parent, v)
        if x != y:
            resultado.append((u, v, w))
            e += 1
            union(parent, rank, x, y)
    return resultado

if __name__ == "__main__":
    V = 4
    aristas = [
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    print("Árbol de expansión mínimo:", kruskal(V, aristas))
