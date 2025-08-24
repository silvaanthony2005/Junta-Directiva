"""
Rabin-Karp
==========

Teoría:
-------
Usa hash de cadenas para buscar múltiples patrones de manera eficiente.

Complejidad:
------------
- O(n+m) promedio

Uso ideal:
----------
- Búsqueda múltiple de patrones.

Recomendaciones:
----------------
Usar para búsqueda de varios patrones o detección rápida de coincidencias.
"""
def rabin_karp(texto, patron):
    n, m = len(texto), len(patron)
    d = 256
    q = 101
    h = pow(d, m-1) % q
    p = 0
    t = 0
    for i in range(m):
        p = (d * p + ord(patron[i])) % q
        t = (d * t + ord(texto[i])) % q
    for s in range(n - m + 1):
        if p == t:
            if texto[s:s+m] == patron:
                return s
        if s < n - m:
            t = (d * (t - ord(texto[s]) * h) + ord(texto[s + m])) % q
            if t < 0:
                t += q
    return -1

if __name__ == "__main__":
    texto = "GEEKS FOR GEEKS"
    patron = "FOR"
    print(f"Índice de '{patron}':", rabin_karp(texto, patron))
