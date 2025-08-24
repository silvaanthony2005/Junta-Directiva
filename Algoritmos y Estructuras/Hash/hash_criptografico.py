"""
Hash Criptográfico (SHA-256)
===========================

Teoría:
-------
Función hash diseñada para seguridad, irreversibilidad y resistencia a colisiones. Muy usada en integridad de archivos y criptomonedas.

Complejidad:
------------
- O(n)

Uso ideal:
----------
- Firmas digitales, integridad de archivos, contraseñas.

Recomendaciones:
----------------
No usar para tablas hash comunes, solo para seguridad.
"""
import hashlib

def hash_sha256(texto):
    return hashlib.sha256(texto.encode()).hexdigest()

if __name__ == "__main__":
    texto = "algoritmos"
    print(f"SHA-256 de '{texto}':", hash_sha256(texto))
