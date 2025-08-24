# Algoritmos de Programación Dinámica: Teoría, Comparativa y Casos de Uso

## ¿Qué es la Programación Dinámica?
La programación dinámica (PD) es una técnica de diseño algorítmico que resuelve problemas dividiéndolos en subproblemas más pequeños, almacenando los resultados de estos subproblemas para evitar cálculos repetidos.

## Problemas Clásicos y Comparativa

| Problema                  | Complejidad     | Tipo      | Uso ideal                                 | Características principales |
|---------------------------|-----------------|-----------|--------------------------------------------|----------------------------|
| Fibonacci                 | O(n)           | 1D        | Secuencias, recursión optimizada           | Subproblemas solapados     |
| Mochila 0/1 (Knapsack)    | O(nW)          | 2D        | Selección óptima de objetos con peso/valor | Tabla DP, decisiones binarias |
| Subcadena común más larga | O(n*m)         | 2D        | Comparación de secuencias                  | Matriz DP, reconstrucción  |
| Cambio de monedas         | O(n*m)         | 1D        | Mínimas monedas para un monto              | Subproblemas de suma       |
| Corte de varilla          | O(n²)          | 1D        | Máximo beneficio de cortes                 | Decisión óptima en cortes  |

---

## Descripción y Recomendaciones

### Fibonacci (DP)
- **Teoría:** Calcula el n-ésimo número de Fibonacci usando almacenamiento de resultados previos.
- **Complejidad:** O(n)
- **Uso ideal:** Secuencias recursivas, optimización de recursión.

### Mochila 0/1 (Knapsack)
- **Teoría:** Selecciona subconjunto de objetos para maximizar valor sin exceder peso.
- **Complejidad:** O(nW)
- **Uso ideal:** Selección óptima bajo restricciones.

### Subcadena común más larga (LCS)
- **Teoría:** Encuentra la secuencia común más larga entre dos cadenas.
- **Complejidad:** O(n*m)
- **Uso ideal:** Comparación de secuencias, bioinformática.

### Cambio de monedas
- **Teoría:** Calcula el mínimo número de monedas para un monto dado.
- **Complejidad:** O(n*m)
- **Uso ideal:** Problemas de suma y combinatoria.

### Corte de varilla
- **Teoría:** Maximiza el beneficio al cortar una varilla en piezas.
- **Complejidad:** O(n²)
- **Uso ideal:** Decisiones óptimas en cortes o divisiones.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
