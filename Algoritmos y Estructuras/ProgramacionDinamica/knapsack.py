"""
Mochila 0/1 (Knapsack)
======================

Teoría:
-------
Selecciona subconjunto de objetos para maximizar valor sin exceder peso, usando una tabla DP.

Complejidad:
------------
- O(nW)

Uso ideal:
----------
- Selección óptima bajo restricciones.

Recomendaciones:
----------------
Usar cuando se requiere maximizar valor bajo una restricción de peso.
"""
def knapsack(weights, values, W):
    n = len(values)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    W = 50
    print("Valor máximo en la mochila:", knapsack(weights, values, W))
