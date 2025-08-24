"""
Cambio de monedas (Greedy)
=========================

Teoría:
-------
Selecciona la moneda de mayor valor posible en cada paso hasta alcanzar el monto.

Complejidad:
------------
- O(n)

Uso ideal:
----------
- Sistemas de monedas canónicos (como el euro o dólar).

Recomendaciones:
----------------
No siempre funciona para sistemas de monedas no canónicos.
"""
def cambio_monedas_greedy(monedas, monto):
    monedas.sort(reverse=True)
    resultado = []
    for moneda in monedas:
        while monto >= moneda:
            monto -= moneda
            resultado.append(moneda)
    return resultado

if __name__ == "__main__":
    monedas = [1, 5, 10, 25]
    monto = 63
    print("Monedas usadas:", cambio_monedas_greedy(monedas, monto))
