# Importa la biblioteca copy para copiar objetos
import copy

# Define la función heurística
def heuristica(tablero):
    # Cuenta el número de bloques que están en la posición correcta
    correctos = 0
    for i in range(len(tablero)):
        if tablero[i] == i:
            correctos += 1
    # Devuelve el número de bloques que están en la posición correcta
    return correctos

# Define la función para mover un bloque desde una torre a otra torre
def mover_bloque(tablero, origen, destino):
    # Copia el tablero original para no modificarlo directamente
    nuevo_tablero = copy.deepcopy(tablero)
    # Encuentra el índice del bloque en la torre de origen
    bloque = nuevo_tablero[origen].pop()
    # Agrega el bloque a la torre de destino
    nuevo_tablero[destino].append(bloque)
    # Devuelve el nuevo tablero con el bloque movido
    return nuevo_tablero

# Define la función para encontrar la solución utilizando el algoritmo de ascenso de colinas
def encontrar_solucion(tablero):
    # Define una variable para contar el número de movimientos necesarios para llegar a la solución
    movimientos = 0
    # Repite hasta que se encuentre la solución o se alcance un máximo número de iteraciones
    while True:
        # Calcula la heurística del tablero actual
        h_actual = heuristica(tablero)
        # Si la heurística es cero, se ha encontrado la solución
        if h_actual == 0:
            print("Solución encontrada en", movimientos, "movimientos.")
            return tablero
        # Define una variable para almacenar el mejor movimiento encontrado hasta ahora
        mejor_movimiento = None
        mejor_h = h_actual
        # Prueba todos los posibles movimientos desde cada torre a cada otra torre
        for origen in range(3):
            for destino in range(3):
                if origen != destino and len(tablero[origen]) > 0:
                    nuevo_tablero = mover_bloque(tablero, origen, destino)
                    h_nuevo = heuristica(nuevo_tablero)
                    if h_nuevo < mejor_h:
                        mejor_movimiento = (origen, destino)
                        mejor_h = h_nuevo
        # Si se encontró un mejor movimiento, muévelo y actualiza el contador de movimientos
        if mejor_movimiento is not None:
            tablero = mover_bloque(tablero, *mejor_movimiento)
            movimientos += 1
        # Si no se encontró un mejor movimiento, se ha llegado a un máximo local y se debe reiniciar con un nuevo tablero aleatorio
        else:
            print("Reiniciando con un nuevo tablero aleatorio.")
            tablero = [[2, 1, 0], [], []]
            movimientos = 0

# Define un tablero inicial aleatorio y encuentra la solución utilizando el algoritmo de ascenso de colinas y la función heurística definida anteriormente.
tablero_inicial = [[2, 1, 0], [], []]
encontrar_solucion(tablero_inicial)