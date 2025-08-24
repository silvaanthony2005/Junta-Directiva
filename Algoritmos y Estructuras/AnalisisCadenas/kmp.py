"""
KMP (Knuth-Morris-Pratt)
=======================

Teoría:
-------
Preprocesa el patrón para evitar comparaciones redundantes usando un arreglo de prefijos.

Complejidad:
------------
- O(n+m)

Uso ideal:
----------
- Búsqueda eficiente de patrones en textos largos.

Recomendaciones:
----------------
Usar cuando el patrón es largo o se realizan muchas búsquedas.
"""
def kmp(texto, patron):
    def calcular_lps(patron):
        lps = [0] * len(patron)
        length = 0
        i = 1
        while i < len(patron):
            if patron[i] == patron[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps
    n, m = len(texto), len(patron)
    lps = calcular_lps(patron)
    i = j = 0
    while i < n:
        if texto[i] == patron[j]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and texto[i] != patron[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1

if __name__ == "__main__":
    texto = "abxabcabcaby"
    patron = "abcaby"
    print(f"Índice de '{patron}':", kmp(texto, patron))
