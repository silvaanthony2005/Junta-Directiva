"""
Selección de actividades (Activity Selection)
============================================

Teoría:
-------
Selecciona la actividad que termina más temprano y es compatible con las ya seleccionadas.

Complejidad:
------------
- O(n log n)

Uso ideal:
----------
- Programación de tareas, uso de recursos.

Recomendaciones:
----------------
Ordenar actividades por tiempo de finalización.
"""
def seleccion_actividades(inicio, fin):
    actividades = sorted(zip(inicio, fin), key=lambda x: x[1])
    resultado = [actividades[0]]
    for act in actividades[1:]:
        if act[0] >= resultado[-1][1]:
            resultado.append(act)
    return resultado

if __name__ == "__main__":
    inicio = [1, 3, 0, 5, 8, 5]
    fin = [2, 4, 6, 7, 9, 9]
    print("Actividades seleccionadas:", seleccion_actividades(inicio, fin))
