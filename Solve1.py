from copy import deepcopy

# Función para calcular la heurística del estado actual
def heuristic(current_state):
    h = 0
    for i, stack in enumerate(current_state):
        for j, block in enumerate(stack):
            if block != "C":
                h += 1
            if j > 0 and stack[j-1] != "C" and block != "C":
                h += 1
            if i > 0:
                for k in range(len(current_state[i-1])):
                    if current_state[i-1][k] != "C" and block != "C":
                        h += 1
    return h

# Estado inicial
current = [["B", "A", "C"], [], []]

# Estado objetivo
goal = [["A", "B", "C"], [], []]

# Número máximo de iteraciones
max_iterations = 1000

# Lista para almacenar los movimientos realizados
moves = []

# Realizar búsqueda por ascenso de colinas
for i in range(max_iterations):
    # Calcular la heurística del estado actual
    h_current = heuristic(current)
    
    # Si el estado actual es el objetivo, detener la búsqueda
    if current == goal:
        print("Solución encontrada:")
        for move in moves:
            print(move)
        print("Número de movimientos:", len(moves))
        break
    
    # Encontrar el mejor vecino
    best_neighbor = None
    best_neighbor_h = float("inf")
    best_neighbor_index = None
    for i, stack in enumerate(current):
        if len(stack) > 0:
            for j in range(len(current)):
                if i != j:
                    # Intentar mover el bloque superior de la pila i a la pila j
                    neighbor = deepcopy(current)
                    block = neighbor[i].pop()
                    neighbor[j].append(block)
                    
                    # Calcular la heurística del vecino
                    h_neighbor = heuristic(neighbor)
                    
                    # Si el vecino es mejor que el mejor vecino encontrado hasta ahora, actualizar
                    if h_neighbor < best_neighbor_h:
                        best_neighbor = neighbor
                        best_neighbor_h = h_neighbor
                        best_neighbor_index = j
    
    # Si no se encontró un mejor vecino, detener la búsqueda
    if best_neighbor_h >= h_current:
        print("Se alcanzó un máximo local.")
        break
    
    # Realizar el movimiento al mejor vecino encontrado
    moves.append(f"Move block {current[best_neighbor_index][-1]} from stack {current.index(current[best_neighbor_index])+1} to stack {best_neighbor_index+1}")
    current = best_neighbor
