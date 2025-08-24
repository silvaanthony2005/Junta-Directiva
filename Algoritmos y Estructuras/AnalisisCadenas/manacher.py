"""
Palíndromos (Manacher)
=====================

Teoría:
-------
Encuentra la subcadena palíndroma más larga en tiempo lineal.

Complejidad:
------------
- O(n)

Uso ideal:
----------
- Detección de palíndromos en cadenas largas.

Recomendaciones:
----------------
Usar para encontrar palíndromos en tiempo eficiente.
"""
def manacher(s):
    A = '@#' + '#'.join(s) + '#$'
    Z = [0] * len(A)
    center = right = 0
    for i in range(1, len(A) - 1):
        if i < right:
            Z[i] = min(right - i, Z[2 * center - i])
        while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
            Z[i] += 1
        if i + Z[i] > right:
            center, right = i, i + Z[i]
    max_len = max(Z)
    center_index = Z.index(max_len)
    start = (center_index - max_len) // 2
    return s[start:start + max_len]

if __name__ == "__main__":
    s = "babad"
    print("Palíndromo más largo:", manacher(s))
