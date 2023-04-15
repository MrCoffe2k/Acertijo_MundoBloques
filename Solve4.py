from random import shuffle

# Definir estado inicial y estado objetivo como una matriz
estado_inicial = [["B", "A", "C"], [], []]
estado_objetivo = [[], ["A", "B", "C"], []]

# Definir función heurística
def heuristica(estado_actual):
    # Contar número de bloques que están en la posición correcta
    return sum([1 if estado_actual[i][j] == estado_objetivo[i][j] else 0 for i in range(3) for j in range(len(estado_actual[i]))])

# Definir función para generar sucesores
def generar_sucesores(estado_actual, estados_visitados, n=1):
    sucesores = []
    for i in range(3):
        for j in range(3):
            if len(estado_actual[i]) > 0 and (len(estado_actual[j]) == 0 or estado_actual[i][-1] < estado_actual[j][-1]):
                # Mover el bloque de la parte superior de la pila i a la parte superior de la pila j
                sucesor = [estado_actual[k][:] for k in range(3)]
                sucesor[j].append(sucesor[i].pop())
                if sucesor not in estados_visitados: # Verificar si el sucesor ya fue visitado
                    sucesores.append(sucesor)
                    if len(sucesores) >= n: # Detener si ya se generaron suficientes sucesores
                        return sucesores
    return sucesores

# Aplicar estrategia de ascenso de colinas con heurística
movimientos = 0
estado_actual = estado_inicial[:]
estados_visitados = [estado_actual]
while estado_actual != estado_objetivo:
    # Generar un sucesor y calcular su valor heurístico
    sucesor = generar_sucesores(estado_actual, estados_visitados, n=1)[0]
    valor_heuristico = heuristica(sucesor)

    # Verificar si el sucesor tiene un valor heurístico mejor que el actual
    if valor_heuristico < heuristica(estado_actual):
        estado_actual = sucesor[:]
        estados_visitados.append(estado_actual)
        movimientos += 1
        print("Movimiento", movimientos, ": ", estado_actual)
    else:
        # Si no hay sucesor mejor, se barajan los bloques y se intenta de nuevo
        shuffle(estado_actual[0])
        estados_visitados.append(estado_actual)
        movimientos += 1
        print("Movimiento", movimientos, ": ", estado_actual)

# Imprimir solución
print("Solución encontrada en", movimientos, "movimientos.")
