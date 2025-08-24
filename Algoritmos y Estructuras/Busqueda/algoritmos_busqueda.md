# Algoritmos de Búsqueda: Teoría, Comparativa y Casos de Uso

## Tabla Comparativa

| Algoritmo             | Complejidad (Promedio) | Requiere orden | Casos de uso ideales                  | Cuándo usarlo |
|-----------------------|-----------------------|----------------|---------------------------------------|---------------|
| Búsqueda Lineal       | O(n)                  | No             | Listas pequeñas o no ordenadas        | Cuando la lista es pequeña o no está ordenada |
| Búsqueda Binaria      | O(log n)              | Sí             | Listas grandes y ordenadas            | Cuando la lista está ordenada |
| Búsqueda Exponencial  | O(log i)              | Sí             | Listas muy grandes y ordenadas        | Cuando no se conoce el tamaño exacto de la lista |
| Búsqueda por Interpolación | O(log log n)     | Sí             | Listas ordenadas y distribuidas uniformemente | Cuando los datos son numéricos y uniformes |
| Búsqueda en Saltos (Jump Search) | O(√n)      | Sí             | Listas ordenadas                      | Cuando se busca simplicidad y eficiencia en listas ordenadas |
| Búsqueda Fibonacci    | O(log n)              | Sí             | Listas ordenadas                      | Alternativa a la binaria, útil en hardware con acceso secuencial |

---

## Descripción y Recomendaciones

### Búsqueda Lineal
- **Teoría:** Recorre la lista elemento por elemento hasta encontrar el objetivo.
- **Complejidad:** O(n)
- **Requiere orden:** No
- **Casos de uso:** Listas pequeñas o no ordenadas.
- **Recomendación:** Útil cuando la lista es pequeña o no está ordenada.

### Búsqueda Binaria
- **Teoría:** Divide la lista ordenada a la mitad repetidamente para encontrar el objetivo.
- **Complejidad:** O(log n)
- **Requiere orden:** Sí
- **Casos de uso:** Listas grandes y ordenadas.
- **Recomendación:** Usar siempre que la lista esté ordenada.

### Búsqueda Exponencial
- **Teoría:** Encuentra un rango exponencialmente y luego aplica búsqueda binaria.
- **Complejidad:** O(log i), donde i es la posición del objetivo.
- **Requiere orden:** Sí
- **Casos de uso:** Listas muy grandes y ordenadas, tamaño desconocido.
- **Recomendación:** Cuando no se conoce el tamaño exacto de la lista.

### Búsqueda por Interpolación
- **Teoría:** Estima la posición probable del objetivo usando interpolación.
- **Complejidad:** O(log log n) mejor caso, O(n) peor caso.
- **Requiere orden:** Sí
- **Casos de uso:** Listas ordenadas y distribuidas uniformemente.
- **Recomendación:** Cuando los datos son numéricos y uniformes.

### Búsqueda en Saltos (Jump Search)
- **Teoría:** Salta bloques de tamaño fijo y luego realiza búsqueda lineal en el bloque.
- **Complejidad:** O(√n)
- **Requiere orden:** Sí
- **Casos de uso:** Listas ordenadas.
- **Recomendación:** Alternativa simple a la búsqueda binaria.

### Búsqueda Fibonacci
- **Teoría:** Utiliza números de Fibonacci para dividir la lista y buscar el objetivo.
- **Complejidad:** O(log n)
- **Requiere orden:** Sí
- **Casos de uso:** Listas ordenadas, hardware con acceso secuencial.
- **Recomendación:** Útil en sistemas donde la búsqueda binaria no es eficiente.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
