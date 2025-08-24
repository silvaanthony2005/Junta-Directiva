"""
Bucket Sort
===========

Teoría:
-------
Bucket Sort distribuye los elementos en varios "cubos" (buckets) según su valor, luego ordena cada cubo (usualmente con Insertion Sort) y finalmente concatena los cubos.

Complejidad:
------------
- Promedio: O(n + k)
- Peor caso: O(n²) (si todos los elementos caen en el mismo cubo)

Estabilidad:
------------
Estable (si el algoritmo interno es estable).

Casos de uso ideales:
---------------------
- Datos uniformemente distribuidos, flotantes.

Recomendaciones:
----------------
Útil cuando los datos están distribuidos uniformemente en un rango conocido.
"""

def bucket_sort(arr):
    if len(arr) == 0:
        return arr
    bucket_count = 10
    min_value = min(arr)
    max_value = max(arr)
    bucket_range = (max_value - min_value) / bucket_count
    buckets = [[] for _ in range(bucket_count)]
    for num in arr:
        index = int((num - min_value) / bucket_range)
        if index == bucket_count:
            index -= 1
        buckets[index].append(num)
    for bucket in buckets:
        bucket.sort()
    result = []
    for bucket in buckets:
        result.extend(bucket)
    return result

if __name__ == "__main__":
    ejemplo = [0.42, 4.21, 3.14, 2.71, 1.61, 0.99, 2.18]
    print("Lista original:", ejemplo)
    print("Lista ordenada:", bucket_sort(ejemplo))
