# Definición del estado inicial y estado meta
estado_inicial = ["B", "A", "C"]
estado_meta = ["A", "B", "C"]

# Función para calcular la heurística
def heuristica(estado):
    # Cada bloque fuera de su posición meta cuenta como 1 en la heurística
    h = 0
    for i in range(len(estado)):
        if estado[i] != estado_meta[i]:
            h += 1
    return h

# Función para generar vecinos
def generar_vecinos(estado):
    vecinos = []
    for i in range(len(estado)):
        for j in range(len(estado)):
            if i != j:
                vecino = estado.copy()
                bloque = vecino.pop(i)
                vecino.insert(j, bloque)
                vecinos.append(vecino)
    return vecinos

# Algoritmo de ascenso de colinas con función heurística
estado_actual = estado_inicial
movimientos = 0
while True:
    h_actual = heuristica(estado_actual)
    if h_actual == 0:
        # Solución encontrada
        print("Se ha encontrado la solución en", movimientos, "movimientos:")
        print(estado_actual)
        break
    vecinos = generar_vecinos(estado_actual)
    mejor_vecino = None
    mejor_h = h_actual
    for vecino in vecinos:
        h_vecino = heuristica(vecino)
        if h_vecino < mejor_h:
            mejor_vecino = vecino
            mejor_h = h_vecino
    if mejor_vecino is None:
        # Estancamiento en óptimo local
        print("Se ha llegado a un óptimo local en", movimientos, "movimientos:")
        print(estado_actual)
        break
    estado_actual = mejor_vecino
    movimientos += 1
    print("Movimiento", movimientos, ":", estado_actual)
