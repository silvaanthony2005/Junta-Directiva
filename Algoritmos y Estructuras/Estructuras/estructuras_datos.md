# Estructuras de Datos: Teoría, Tipos y Casos de Uso

## ¿Qué es una Estructura de Datos?
Una estructura de datos es una forma de organizar y almacenar datos en la memoria de una computadora para que puedan ser utilizados de manera eficiente. Permiten realizar operaciones como inserción, eliminación, búsqueda y recorrido de manera óptima según el tipo de problema.

## Tipos Clásicos y Comparativa

| Estructura      | Operaciones principales | Complejidad promedio | Uso ideal                        | Características principales |
|-----------------|------------------------|---------------------|-----------------------------------|----------------------------|
| Lista (Array)   | Acceso, inserción, borrado | Acceso: O(1), inserción/borrado: O(n) | Almacenamiento secuencial, acceso rápido | Tamaño fijo, memoria contigua |
| Lista enlazada  | Inserción, borrado, recorrido | O(1) inserción/borrado al inicio, O(n) búsqueda | Cuando se requiere inserción/borrado frecuente | Tamaño dinámico, nodos enlazados |
| Pila (Stack)    | push, pop, top         | O(1)                | Algoritmos recursivos, deshacer operaciones | LIFO (último en entrar, primero en salir) |
| Cola (Queue)    | enqueue, dequeue, front | O(1)                | Procesamiento por turnos, BFS     | FIFO (primero en entrar, primero en salir) |
| Árbol binario   | inserción, búsqueda, recorrido | O(log n) promedio | Jerarquías, búsquedas rápidas    | Estructura jerárquica, nodos hijos |
| Árbol AVL/Balanceado | inserción, búsqueda, borrado | O(log n) | Búsqueda eficiente, datos ordenados | Auto-balanceo tras operaciones |
| Heap (Montículo)| inserción, extracción mínimo/máximo | O(log n) | Colas de prioridad, algoritmos greedy | Árbol binario parcial, acceso rápido al extremo |
| Tabla hash      | inserción, búsqueda, borrado | O(1) promedio      | Diccionarios, conjuntos          | Acceso rápido, manejo de colisiones |
| Grafo           | inserción, recorrido, búsqueda | Depende de la representación | Modelar relaciones complejas | Nodos y aristas, dirigido/no dirigido |

---

## Descripción y Recomendaciones

### Lista (Array)
- **Teoría:** Estructura secuencial de tamaño fijo, acceso rápido por índice.
- **Uso ideal:** Cuando se conoce el tamaño y se requiere acceso rápido.

### Lista enlazada
- **Teoría:** Nodos conectados entre sí, tamaño dinámico.
- **Uso ideal:** Inserciones/borrados frecuentes, tamaño variable.

### Pila (Stack)
- **Teoría:** LIFO, operaciones en un solo extremo.
- **Uso ideal:** Algoritmos recursivos, deshacer operaciones.

### Cola (Queue)
- **Teoría:** FIFO, operaciones en extremos opuestos.
- **Uso ideal:** Procesamiento por turnos, algoritmos BFS.

### Árbol binario
- **Teoría:** Cada nodo tiene hasta dos hijos, estructura jerárquica.
- **Uso ideal:** Búsqueda, jerarquías, ordenamientos.

### Árbol AVL/Balanceado
- **Teoría:** Árbol binario que se auto-balancea tras inserciones/borrados.
- **Uso ideal:** Búsqueda eficiente en datos ordenados.

### Heap (Montículo)
- **Teoría:** Árbol binario parcial, acceso rápido al mínimo/máximo.
- **Uso ideal:** Colas de prioridad, algoritmos greedy.

### Tabla hash
- **Teoría:** Usa función hash para acceso rápido.
- **Uso ideal:** Diccionarios, conjuntos.

### Grafo
- **Teoría:** Conjunto de nodos y aristas, modela relaciones complejas.
- **Uso ideal:** Redes, mapas, relaciones.

---

Cada estructura tendrá su propio archivo Python con implementación y explicación detallada.
