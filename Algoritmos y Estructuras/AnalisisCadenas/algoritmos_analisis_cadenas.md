# Algoritmos de Análisis de Cadenas: Teoría, Comparativa y Casos de Uso

## ¿Qué es el Análisis de Cadenas?
El análisis de cadenas consiste en buscar, comparar, analizar patrones o extraer información de textos o secuencias de caracteres. Es fundamental en procesamiento de texto, bioinformática, compiladores y más.

## Problemas Clásicos y Comparativa

| Algoritmo                  | Complejidad     | Uso ideal                                 | Características principales |
|----------------------------|-----------------|--------------------------------------------|----------------------------|
| Búsqueda ingenua (Naive)   | O(n*m)         | Textos pequeños, casos simples             | Comparación directa        |
| KMP (Knuth-Morris-Pratt)   | O(n+m)         | Búsqueda eficiente de patrones             | Preprocesa el patrón       |
| Boyer-Moore                | O(n) promedio  | Búsqueda rápida en textos grandes          | Salta posiciones           |
| Rabin-Karp                 | O(n+m) promedio| Búsqueda múltiple de patrones              | Usa hash de cadenas        |
| Palíndromos (Manacher)     | O(n)           | Detección de subcadenas palíndromas        | Expande alrededor del centro|
| Subcadena común más larga (LCS) | O(n*m)    | Comparación de secuencias                  | Programación dinámica      |

---

## Descripción y Recomendaciones

### Búsqueda ingenua (Naive)
- **Teoría:** Compara el patrón con cada posición posible en el texto.
- **Complejidad:** O(n*m)
- **Uso ideal:** Textos pequeños o casos simples.

### KMP (Knuth-Morris-Pratt)
- **Teoría:** Preprocesa el patrón para evitar comparaciones redundantes.
- **Complejidad:** O(n+m)
- **Uso ideal:** Búsqueda eficiente de patrones en textos largos.

### Boyer-Moore
- **Teoría:** Salta posiciones en el texto usando información del patrón.
- **Complejidad:** O(n) promedio
- **Uso ideal:** Textos grandes, búsqueda rápida.

### Rabin-Karp
- **Teoría:** Usa hash de cadenas para buscar múltiples patrones.
- **Complejidad:** O(n+m) promedio
- **Uso ideal:** Búsqueda múltiple de patrones.

### Palíndromos (Manacher)
- **Teoría:** Encuentra la subcadena palíndroma más larga en tiempo lineal.
- **Complejidad:** O(n)
- **Uso ideal:** Detección de palíndromos en cadenas largas.

### Subcadena común más larga (LCS)
- **Teoría:** Encuentra la secuencia común más larga entre dos cadenas.
- **Complejidad:** O(n*m)
- **Uso ideal:** Comparación de secuencias, bioinformática.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
