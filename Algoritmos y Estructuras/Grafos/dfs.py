"""
Búsqueda en Profundidad (DFS)
============================

Teoría:
-------
Explora tan profundo como sea posible antes de retroceder. Puede implementarse de forma recursiva o con una pila explícita.

Complejidad:
------------
- O(V + E)

Uso ideal:
----------
- Detección de ciclos.
- Componentes conexas.
- Orden topológico.

Recomendaciones:
----------------
Usar para análisis estructural del grafo o cuando se requiere explorar todos los caminos posibles.
"""
def dfs(grafo, inicio, visitado=None, recorrido=None):
    if visitado is None:
        visitado = set()
    if recorrido is None:
        recorrido = []
    visitado.add(inicio)
    recorrido.append(inicio)
    for vecino in grafo[inicio]:
        if vecino not in visitado:
            dfs(grafo, vecino, visitado, recorrido)
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
    print("Recorrido DFS desde 'A':", dfs(grafo, 'A'))
