"""
Subcadena común más larga (LCS)
==============================

Teoría:
-------
Encuentra la secuencia común más larga entre dos cadenas usando programación dinámica.

Complejidad:
------------
- O(n*m)

Uso ideal:
----------
- Comparación de secuencias, bioinformática.

Recomendaciones:
----------------
Usar para comparar secuencias o cadenas.
"""
def lcs(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])
    return dp[m][n]

if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    print("Longitud de la LCS:", lcs(X, Y))
