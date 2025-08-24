# Algoritmos de Caminos Mínimos: Teoría, Comparativa y Casos de Uso

## Tabla Comparativa

| Algoritmo      | Complejidad         | Pesos negativos | Uso ideal                                 | Características principales |
|----------------|---------------------|-----------------|--------------------------------------------|----------------------------|
| Dijkstra       | O((V + E) log V)    | No              | Caminos más cortos en grafos con pesos positivos | Usa cola de prioridad, eficiente |
| Bellman-Ford   | O(V * E)            | Sí              | Caminos más cortos con posibles pesos negativos | Detecta ciclos negativos |
| Floyd-Warshall | O(V³)               | Sí              | Todos los pares de caminos más cortos           | Matriz de distancias, grafos densos |

---

## Descripción y Recomendaciones

### Dijkstra
- **Teoría:** Encuentra el camino más corto desde un nodo origen a todos los demás en grafos con pesos no negativos.
- **Complejidad:** O((V + E) log V)
- **Pesos negativos:** No
- **Uso ideal:** Rutas más cortas en mapas, redes, etc.
- **Recomendación:** Usar cuando todos los pesos son positivos.

### Bellman-Ford
- **Teoría:** Permite encontrar caminos más cortos incluso con pesos negativos y detecta ciclos negativos.
- **Complejidad:** O(V * E)
- **Pesos negativos:** Sí
- **Uso ideal:** Cuando hay posibilidad de pesos negativos.
- **Recomendación:** Usar si existen aristas con peso negativo o se requiere detectar ciclos negativos.

### Floyd-Warshall
- **Teoría:** Calcula los caminos más cortos entre todos los pares de nodos.
- **Complejidad:** O(V³)
- **Pesos negativos:** Sí
- **Uso ideal:** Grafos densos, todos los pares de caminos más cortos.
- **Recomendación:** Usar para grafos pequeños o medianos donde se requiere conocer todos los caminos mínimos.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
