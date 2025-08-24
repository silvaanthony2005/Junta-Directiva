"""
Hashing Cerrado (Open Addressing, Sondeo Lineal)
===============================================

Teoría:
-------
Si hay colisión, se busca la siguiente posición libre en el arreglo (sondeo lineal).

Complejidad:
------------
- O(1) promedio, O(n) peor caso

Uso ideal:
----------
- Cuando se quiere evitar estructuras adicionales.

Recomendaciones:
----------------
No llenar la tabla más del 70% para evitar muchas colisiones.
"""
class OpenAddressingHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        idx = self._hash(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None or self.table[probe][0] == key:
                self.table[probe] = (key, value)
                return
        raise Exception("Tabla llena")

    def search(self, key):
        idx = self._hash(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None:
                return None
            if self.table[probe][0] == key:
                return self.table[probe][1]
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i in range(self.size):
            probe = (idx + i) % self.size
            if self.table[probe] is None:
                return
            if self.table[probe][0] == key:
                self.table[probe] = None
                return

if __name__ == "__main__":
    ht = OpenAddressingHashTable()
    ht.insert("manzana", 1)
    ht.insert("banana", 2)
    print("Buscar 'banana':", ht.search("banana"))
    ht.delete("banana")
    print("Buscar 'banana' tras borrar:", ht.search("banana"))
