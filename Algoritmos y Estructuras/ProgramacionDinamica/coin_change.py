"""
Cambio de monedas (Coin Change)
==============================

Teoría:
-------
Calcula el mínimo número de monedas para un monto dado usando DP.

Complejidad:
------------
- O(n*m)

Uso ideal:
----------
- Problemas de suma y combinatoria.

Recomendaciones:
----------------
Usar para encontrar la mínima cantidad de monedas para un monto.
"""
def coin_change(monedas, monto):
    dp = [float('inf')] * (monto + 1)
    dp[0] = 0
    for coin in monedas:
        for x in range(coin, monto + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)
    return dp[monto] if dp[monto] != float('inf') else -1

if __name__ == "__main__":
    monedas = [1, 2, 5]
    monto = 11
    print("Mínimo número de monedas:", coin_change(monedas, monto))
