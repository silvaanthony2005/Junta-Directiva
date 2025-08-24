# Algoritmos Codiciosos: Teoría, Comparativa y Casos de Uso

## ¿Qué es un Algoritmo Codicioso?
Un algoritmo codicioso (greedy) toma decisiones óptimas locales en cada paso con la esperanza de encontrar una solución global óptima. No siempre garantiza la mejor solución para todos los problemas, pero es eficiente y simple para muchos casos clásicos.

## Problemas Clásicos y Comparativa

| Problema                  | Complejidad     | Uso ideal                                 | Características principales |
|---------------------------|-----------------|--------------------------------------------|----------------------------|
| Cambio de monedas (greedy)| O(n)           | Monedas con sistema canónico               | Selección local óptima     |
| Actividades máximas       | O(n log n)     | Selección de actividades no solapadas      | Ordenar por fin, elegir compatible |
| Árbol de expansión mínimo (Kruskal/Prim) | O(E log V) | Redes, grafos conectados | Selección de aristas mínimas |
| Caminos más cortos (Dijkstra) | O((V+E) log V) | Pesos positivos | Selección de nodo más cercano |
| Huffman (codificación)    | O(n log n)     | Compresión de datos                       | Construcción de árbol óptimo |

---

## Descripción y Recomendaciones

### Cambio de monedas (Greedy)
- **Teoría:** Selecciona la moneda de mayor valor posible en cada paso.
- **Complejidad:** O(n)
- **Uso ideal:** Sistemas de monedas canónicos (como el euro o dólar).

### Selección de actividades
- **Teoría:** Selecciona la actividad que termina más temprano y es compatible con las ya seleccionadas.
- **Complejidad:** O(n log n)
- **Uso ideal:** Programación de tareas, uso de recursos.

### Árbol de expansión mínimo (Kruskal/Prim)
- **Teoría:** Selecciona aristas de menor peso que no formen ciclos hasta conectar todos los nodos.
- **Complejidad:** O(E log V)
- **Uso ideal:** Redes, grafos conectados.

### Caminos más cortos (Dijkstra)
- **Teoría:** Selecciona el nodo más cercano no visitado en cada paso.
- **Complejidad:** O((V+E) log V)
- **Uso ideal:** Pesos positivos.

### Codificación de Huffman
- **Teoría:** Construye un árbol binario óptimo para compresión de datos.
- **Complejidad:** O(n log n)
- **Uso ideal:** Compresión de datos.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
