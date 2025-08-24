"""
Raíz cuadrada entera
===================

Teoría:
-------
Calcula la raíz cuadrada entera usando búsqueda binaria.

Complejidad:
------------
- O(log n)

Uso ideal:
----------
- Cálculo rápido de raíces.

Recomendaciones:
----------------
Usar para encontrar la raíz cuadrada entera de números grandes.
"""
def raiz_cuadrada_entera(n):
    if n < 0:
        raise ValueError("No se puede calcular la raíz cuadrada de un número negativo")
    if n == 0 or n == 1:
        return n
    inicio, fin = 1, n
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if medio * medio == n:
            return medio
        elif medio * medio < n:
            inicio = medio + 1
            res = medio
        else:
            fin = medio - 1
    return res

if __name__ == "__main__":
    print("Raíz cuadrada entera de 27:", raiz_cuadrada_entera(27))
