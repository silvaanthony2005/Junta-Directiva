# Algoritmos de Ordenación: Teoría, Comparativa y Casos de Uso

## Tabla Comparativa

| Algoritmo       | Complejidad (Promedio) | Estabilidad | Casos de uso ideales | Cuándo usarlo |
|-----------------|-----------------------|-------------|----------------------|---------------|
| Bubble Sort     | O(n²)                 | ✅ Estable   | Educación, visualización de conceptos básicos | Solo para enseñanza o listas muy pequeñas |
| Insertion Sort  | O(n²)                 | ✅ Estable   | Listas pequeñas, casi ordenadas | Cuando los datos están casi ordenados o el tamaño es muy reducido |
| Selection Sort  | O(n²)                 | ❌ Inestable | Educación, listas pequeñas sin necesidad de estabilidad | Cuando la estabilidad no importa y se requiere simplicidad |
| Merge Sort      | O(n log n)            | ✅ Estable   | Grandes volúmenes de datos, ordenamiento externo | Cuando se necesita estabilidad y se trabaja con estructuras grandes |
| Quick Sort      | O(n log n)            | ❌ Inestable | Ordenamiento en memoria, listas grandes | Cuando se busca velocidad y no se requiere estabilidad |
| Heap Sort       | O(n log n)            | ❌ Inestable | Sistemas embebidos, sin recursión profunda | Cuando se necesita eficiencia sin usar mucha memoria adicional |
| Tim Sort        | O(n log n)            | ✅ Estable   | Ordenamiento en Python, Java, datos parcialmente ordenados | Ideal para uso general: rápido, estable y adaptativo |
| Radix Sort      | O(nk)                 | ✅ Estable   | Enteros, cadenas de longitud fija | Cuando se ordenan claves numéricas o cadenas con longitud conocida |
| Counting Sort   | O(n + k)              | ✅ Estable   | Enteros en rango pequeño | Cuando los datos son enteros y el rango es limitado |
| Bucket Sort     | O(n + k)              | ✅ Estable   | Distribuciones uniformes, flotantes | Cuando los datos están distribuidos uniformemente en un rango conocido |

---

## Descripción y Recomendaciones

### Bubble Sort
- **Teoría:** Algoritmo sencillo que compara elementos adyacentes e intercambia si están en el orden incorrecto.
- **Complejidad:** O(n²)
- **Estabilidad:** Estable
- **Casos de uso:** Educación, listas muy pequeñas.
- **Recomendación:** No usar en producción, solo para enseñanza.

### Insertion Sort
- **Teoría:** Inserta cada elemento en su posición correcta en una lista parcialmente ordenada.
- **Complejidad:** O(n²), O(n) mejor caso.
- **Estabilidad:** Estable
- **Casos de uso:** Listas pequeñas o casi ordenadas.
- **Recomendación:** Útil para arreglos pequeños o como parte de otros algoritmos.

### Selection Sort
- **Teoría:** Selecciona el elemento más pequeño y lo coloca en la posición correcta.
- **Complejidad:** O(n²)
- **Estabilidad:** Inestable
- **Casos de uso:** Educación, listas pequeñas.
- **Recomendación:** Cuando la estabilidad no es importante.

### Merge Sort
- **Teoría:** Divide y conquista, divide la lista y luego fusiona ordenadamente.
- **Complejidad:** O(n log n)
- **Estabilidad:** Estable
- **Casos de uso:** Grandes volúmenes de datos.
- **Recomendación:** Cuando se requiere estabilidad y eficiencia.

### Quick Sort
- **Teoría:** Divide y conquista, elige un pivote y particiona la lista.
- **Complejidad:** O(n log n) promedio, O(n²) peor caso.
- **Estabilidad:** Inestable
- **Casos de uso:** Listas grandes en memoria.
- **Recomendación:** Muy rápido, pero no estable.

### Heap Sort
- **Teoría:** Utiliza un heap para ordenar los elementos.
- **Complejidad:** O(n log n)
- **Estabilidad:** Inestable
- **Casos de uso:** Sistemas embebidos, poca memoria.
- **Recomendación:** Cuando no se puede usar memoria adicional.

### Tim Sort
- **Teoría:** Mezcla de Merge e Insertion Sort, usado en Python y Java.
- **Complejidad:** O(n log n)
- **Estabilidad:** Estable
- **Casos de uso:** Ordenamiento general, datos parcialmente ordenados.
- **Recomendación:** Algoritmo por defecto en Python y Java.

### Radix Sort
- **Teoría:** Ordena por dígitos o caracteres, de menor a mayor significancia.
- **Complejidad:** O(nk)
- **Estabilidad:** Estable
- **Casos de uso:** Enteros, cadenas de longitud fija.
- **Recomendación:** Cuando el rango de claves es conocido y pequeño.

### Counting Sort
- **Teoría:** Cuenta ocurrencias de cada valor y las posiciona.
- **Complejidad:** O(n + k)
- **Estabilidad:** Estable
- **Casos de uso:** Enteros en rango pequeño.
- **Recomendación:** Cuando el rango de valores es limitado.

### Bucket Sort
- **Teoría:** Distribuye los elementos en "cubetas" y ordena cada una.
- **Complejidad:** O(n + k)
- **Estabilidad:** Estable
- **Casos de uso:** Datos uniformemente distribuidos.
- **Recomendación:** Cuando los datos son flotantes o uniformes.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
