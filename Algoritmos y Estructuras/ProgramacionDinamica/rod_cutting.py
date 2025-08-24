"""
Corte de varilla (Rod Cutting)
==============================

Teoría:
-------
Maximiza el beneficio al cortar una varilla en piezas usando DP.

Complejidad:
------------
- O(n²)

Uso ideal:
----------
- Decisiones óptimas en cortes o divisiones.

Recomendaciones:
----------------
Usar para maximizar beneficio en problemas de corte.
"""
def rod_cutting(precios, n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        max_val = float('-inf')
        for j in range(i):
            max_val = max(max_val, precios[j] + dp[i - j - 1])
        dp[i] = max_val
    return dp[n]

if __name__ == "__main__":
    precios = [1, 5, 8, 9, 10, 17, 17, 20]
    n = len(precios)
    print("Beneficio máximo:", rod_cutting(precios, n))
