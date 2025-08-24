# Algoritmos Recursivos: Teoría, Comparativa y Casos de Uso

## ¿Qué es la Recursión?
La recursión es una técnica donde una función se llama a sí misma para resolver un problema dividiéndolo en subproblemas más pequeños. Es útil para problemas que pueden descomponerse en casos base y casos recursivos.

## Problemas Clásicos y Comparativa

| Problema                  | Complejidad     | Uso ideal                                 | Características principales |
|---------------------------|-----------------|--------------------------------------------|----------------------------|
| Factorial                 | O(n)           | Cálculo de productos sucesivos             | Caso base y recursivo      |
| Fibonacci                 | O(2^n)         | Secuencias, demostración de recursión      | Ineficiente sin DP         |
| Torres de Hanoi           | O(2^n)         | Problemas de movimiento y recursión múltiple| Descomposición en subproblemas |
| Búsqueda binaria recursiva| O(log n)       | Listas ordenadas                          | Divide y vencerás          |
| Permutaciones             | O(n!)          | Generación de combinaciones                | Recursión con backtracking |

---

## Descripción y Recomendaciones

### Factorial
- **Teoría:** Calcula el producto de todos los enteros positivos hasta n.
- **Complejidad:** O(n)
- **Uso ideal:** Matemáticas, combinatoria.

### Fibonacci (recursivo)
- **Teoría:** Suma los dos anteriores para obtener el siguiente número.
- **Complejidad:** O(2^n)
- **Uso ideal:** Demostración de recursión, no para grandes n.

### Torres de Hanoi
- **Teoría:** Mueve n discos de una torre a otra siguiendo reglas específicas.
- **Complejidad:** O(2^n)
- **Uso ideal:** Problemas de movimiento, recursión múltiple.

### Búsqueda binaria recursiva
- **Teoría:** Divide la lista ordenada y busca recursivamente.
- **Complejidad:** O(log n)
- **Uso ideal:** Listas ordenadas.

### Permutaciones
- **Teoría:** Genera todas las posibles ordenaciones de una lista.
- **Complejidad:** O(n!)
- **Uso ideal:** Combinatoria, generación de soluciones.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
