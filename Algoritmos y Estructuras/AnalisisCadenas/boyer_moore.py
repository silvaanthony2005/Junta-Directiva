"""
Boyer-Moore
===========

Teoría:
-------
Salta posiciones en el texto usando información del patrón (bad character rule).

Complejidad:
------------
- O(n) promedio

Uso ideal:
----------
- Textos grandes, búsqueda rápida.

Recomendaciones:
----------------
Usar para textos largos y patrones complejos.
"""
def boyer_moore(texto, patron):
    def bad_char_table(patron):
        tabla = {}
        for i, c in enumerate(patron):
            tabla[c] = i
        return tabla
    n, m = len(texto), len(patron)
    tabla = bad_char_table(patron)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and patron[j] == texto[i + j]:
            j -= 1
        if j < 0:
            return i
        else:
            salto = max(1, j - tabla.get(texto[i + j], -1))
            i += salto
    return -1

if __name__ == "__main__":
    texto = "HERE IS A SIMPLE EXAMPLE"
    patron = "EXAMPLE"
    print(f"Índice de '{patron}':", boyer_moore(texto, patron))
