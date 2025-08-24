"""
Codificación de Huffman
======================

Teoría:
-------
Construye un árbol binario óptimo para compresión de datos, asignando códigos más cortos a los símbolos más frecuentes.

Complejidad:
------------
- O(n log n)

Uso ideal:
----------
- Compresión de datos.

Recomendaciones:
----------------
Usar para compresión eficiente sin pérdida.
"""
import heapq

def huffman(frecuencias):
    heap = [[peso, [simbolo, ""]] for simbolo, peso in frecuencias.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for par in lo[1:]:
            par[1] = '0' + par[1]
        for par in hi[1:]:
            par[1] = '1' + par[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

if __name__ == "__main__":
    frecuencias = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
    print("Códigos Huffman:")
    for simbolo, codigo in huffman(frecuencias):
        print(f"{simbolo}: {codigo}")
