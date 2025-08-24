"""
Permutaciones Recursivas
=======================

Teoría:
-------
Genera todas las posibles ordenaciones de una lista usando recursión y backtracking.

Complejidad:
------------
- O(n!)

Uso ideal:
----------
- Combinatoria, generación de soluciones.

Recomendaciones:
----------------
Usar para problemas de generación de combinaciones y permutaciones.
"""
def permutaciones(arr, path=None, usadas=None, resultado=None):
    if path is None:
        path = []
    if usadas is None:
        usadas = [False] * len(arr)
    if resultado is None:
        resultado = []
    if len(path) == len(arr):
        resultado.append(path[:])
        return resultado
    for i in range(len(arr)):
        if not usadas[i]:
            usadas[i] = True
            path.append(arr[i])
            permutaciones(arr, path, usadas, resultado)
            path.pop()
            usadas[i] = False
    return resultado

if __name__ == "__main__":
    arr = [1, 2, 3]
    print("Permutaciones de [1,2,3]:", permutaciones(arr))
