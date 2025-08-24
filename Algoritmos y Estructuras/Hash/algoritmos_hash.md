# Algoritmos Hash: Teoría, Comparativa y Casos de Uso

## ¿Qué es un Algoritmo Hash?
Un algoritmo hash transforma datos de entrada (de cualquier tamaño) en una cadena de longitud fija, llamada valor hash. Se usan en estructuras de datos (tablas hash), verificación de integridad, criptografía y más.

## Tipos y Comparativa

| Algoritmo/Tipo         | Complejidad Inserción/Búsqueda | Uso ideal                        | Características principales |
|------------------------|-------------------------------|-----------------------------------|----------------------------|
| Tabla Hash (Hash Table)| Promedio: O(1), Peor: O(n)    | Búsqueda rápida, diccionarios     | Colisiones, funciones hash |
| Hashing Abierto        | O(1) promedio                 | Tablas hash con listas enlazadas  | Manejo de colisiones por listas |
| Hashing Cerrado (Open Addressing) | O(1) promedio      | Tablas hash con sondeo lineal/cuadrático | Colisiones en el mismo arreglo |
| Hash Criptográfico     | O(n)                          | Seguridad, integridad de datos    | SHA-256, MD5, irreversibilidad |

---

## Descripción y Recomendaciones

### Tabla Hash
- **Teoría:** Usa una función hash para mapear claves a posiciones en un arreglo.
- **Complejidad:** O(1) promedio, O(n) peor caso (muchas colisiones).
- **Uso ideal:** Diccionarios, conjuntos, búsqueda rápida.

### Hashing Abierto (Separate Chaining)
- **Teoría:** Cada posición de la tabla contiene una lista enlazada de elementos.
- **Uso ideal:** Cuando se esperan muchas colisiones.

### Hashing Cerrado (Open Addressing)
- **Teoría:** Si hay colisión, se busca otra posición libre en el arreglo (lineal, cuadrático, doble hash).
- **Uso ideal:** Cuando se quiere evitar estructuras adicionales.

### Hash Criptográfico
- **Teoría:** Funciones hash diseñadas para seguridad, irreversibilidad y resistencia a colisiones.
- **Uso ideal:** Firmas digitales, integridad de archivos, contraseñas.

---

Cada algoritmo tendrá su propio archivo Python con implementación y explicación detallada.
