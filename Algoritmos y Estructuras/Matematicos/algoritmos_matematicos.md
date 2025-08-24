# Algoritmos Matemáticos: Teoría, Comparativa y Casos de Uso

## ¿Qué son los Algoritmos Matemáticos?
Son algoritmos que resuelven problemas clásicos de matemáticas, como divisibilidad, factorización, aritmética modular, teoría de números, etc. Son fundamentales en criptografía, álgebra, análisis numérico y más.

## Problemas Clásicos y Comparativa

| Algoritmo                  | Complejidad     | Uso ideal                                 | Características principales |
|----------------------------|-----------------|--------------------------------------------|----------------------------|
| Máximo común divisor (MCD) | O(log n)        | Simplificación de fracciones, aritmética   | Algoritmo de Euclides      |
| Mínimo común múltiplo (MCM)| O(log n)        | Operaciones con fracciones                 | Usa MCD                    |
| Criba de Eratóstenes       | O(n log log n)  | Generación de números primos               | Eficiente para primos      |
| Exponenciación rápida      | O(log n)        | Potencias grandes, criptografía            | Divide y vencerás          |
| Números primos             | O(√n)           | Primalidad, factorización                  | Pruebas simples            |
| Raíz cuadrada entera       | O(log n)        | Cálculo rápido de raíces                   | Búsqueda binaria           |

---

## Descripción y Recomendaciones

### Máximo común divisor (MCD)
- **Teoría:** Algoritmo de Euclides para encontrar el mayor divisor común de dos números.
- **Complejidad:** O(log n)
- **Uso ideal:** Simplificación de fracciones, aritmética modular.

### Mínimo común múltiplo (MCM)
- **Teoría:** Calcula el menor múltiplo común usando el MCD.
- **Complejidad:** O(log n)
- **Uso ideal:** Operaciones con fracciones.

### Criba de Eratóstenes
- **Teoría:** Genera todos los números primos hasta n de forma eficiente.
- **Complejidad:** O(n log log n)
- **Uso ideal:** Listas de primos, criptografía.

### Exponenciación rápida
- **Teoría:** Calcula potencias grandes usando divide y vencerás.
- **Complejidad:** O(log n)
- **Uso ideal:** Criptografía, potencias grandes.

### Números primos
- **Teoría:** Prueba si un número es primo comprobando divisores hasta su raíz cuadrada.
- **Complejidad:** O(√n)
- **Uso ideal:** Primalidad, factorización.

### Raíz cuadrada entera
- **Teoría:** Calcula la raíz cuadrada entera usando búsqueda binaria.
- **Complejidad:** O(log n)
- **Uso ideal:** Cálculo rápido de raíces.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
