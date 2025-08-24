# Recorridos de Grafos: Teoría, Comparativa y Casos de Uso

## Tabla Comparativa

| Algoritmo                | Tipo de recorrido | Complejidad | Uso ideal                        | Características principales |
|--------------------------|-------------------|-------------|----------------------------------|----------------------------|
| Búsqueda en Anchura (BFS)| Por niveles       | O(V + E)    | Caminos más cortos en grafos no ponderados, exploración por capas | Usa cola, visita por niveles |
| Búsqueda en Profundidad (DFS)| Profundidad   | O(V + E)    | Detección de ciclos, componentes conexas, topológico | Usa pila (recursión o explícita) |

---

## Descripción y Recomendaciones

### Búsqueda en Anchura (BFS)
- **Teoría:** Recorre el grafo por niveles, visitando primero los vecinos más cercanos al nodo inicial.
- **Complejidad:** O(V + E)
- **Uso ideal:** Encontrar caminos más cortos en grafos no ponderados, exploración por capas.
- **Recomendación:** Usar cuando se necesita el camino más corto o explorar por niveles.

### Búsqueda en Profundidad (DFS)
- **Teoría:** Explora tan profundo como sea posible antes de retroceder.
- **Complejidad:** O(V + E)
- **Uso ideal:** Detección de ciclos, componentes conexas, orden topológico.
- **Recomendación:** Usar para análisis estructural del grafo o cuando se requiere explorar todos los caminos posibles.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
