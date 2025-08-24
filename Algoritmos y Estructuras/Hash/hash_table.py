"""
Tabla Hash (Hash Table) con Hashing Abierto
===========================================

Teoría:
-------
Usa una función hash para mapear claves a posiciones en un arreglo. Cada posición contiene una lista enlazada para manejar colisiones (separate chaining).

Complejidad:
------------
- O(1) promedio, O(n) peor caso

Uso ideal:
----------
- Diccionarios, conjuntos, búsqueda rápida.

Recomendaciones:
----------------
Usar cuando se requiere acceso rápido y se esperan algunas colisiones.
"""
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def search(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        self.table[idx] = [(k, v) for k, v in self.table[idx] if k != key]

if __name__ == "__main__":
    ht = HashTable()
    ht.insert("manzana", 1)
    ht.insert("banana", 2)
    print("Buscar 'manzana':", ht.search("manzana"))
    ht.delete("manzana")
    print("Buscar 'manzana' tras borrar:", ht.search("manzana"))
