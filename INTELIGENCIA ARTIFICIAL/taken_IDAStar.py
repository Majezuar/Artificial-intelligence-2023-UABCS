import math

def manhattan_distance(state, size):
    distance = 0
    for i in range(size):
        for j in range(size):
            value = state[i][j]
            if value != 0:
                row = (value - 1) // size
                col = (value - 1) % size
                distance += abs(row - i) + abs(col - j)
    return distance

def ida_star(start_state, goal_state, size):
    limit = manhattan_distance(start_state, size)
    path = [start_state]
    while True:
        min_limit = math.inf
        last_state = path[-1]
        last_distance = manhattan_distance(last_state, size)
        if last_distance == 0:
            return path
        for neighbor in neighbors(last_state, size):
            neighbor_distance = manhattan_distance(neighbor, size)
            if neighbor_distance + len(path) <= limit and neighbor not in path:
                path.append(neighbor)
                break
            if neighbor_distance + len(path) < min_limit:
                min_limit = neighbor_distance + len(path)
        else:
            path.pop()
        limit = min_limit

def neighbors(state, size):
    zero_row, zero_col = find_zero(state, size)
    for row, col in [(zero_row-1, zero_col), (zero_row+1, zero_col),
                     (zero_row, zero_col-1), (zero_row, zero_col+1)]:
        if 0 <= row < size and 0 <= col < size:
            neighbor = list(map(list, state))
            neighbor[zero_row][zero_col], neighbor[row][col] = neighbor[row][col], neighbor[zero_row][zero_col]
            yield tuple(map(tuple, neighbor))

def find_zero(state, size):
    for i in range(size):
        for j in range(size):
            if state[i][j] == 0:
                return i, j

def print_board(state):
    for row in state:
        print(" ".join(str(x) for x in row))

if __name__ == '__main__':
    size = int(input("Ingrese el tamaño del tablero: "))
    start_state = [[0] * size for _ in range(size)]
    goal_state = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            start_state[i][j] = int(input(f"Ingrese el valor de la casilla ({i+1},{j+1}) del estado inicial: "))
            goal_state[i][j] = int(input(f"Ingrese el valor de la casilla ({i+1},{j+1}) del estado final: "))
    print("Estado inicial:")
    print_board(start_state)
    print("Estado final:")
    print_board(goal_state)
    path = ida_star(tuple(map(tuple, start_state)), tuple(map(tuple, goal_state)), size)
    print("Solución:")
    for state in path:
        print_board(state)
        print()
        
        '''
                Este código implementa el algoritmo IDA* para resolver el juego del 15. El juego del 15 es un rompecabezas en el que se mueven fichas numeradas en una cuadrícula para ordenarlas del 1 al 15. El objetivo del algoritmo es encontrar una secuencia de movimientos que lleve al estado inicial del juego al estado final.

                El código utiliza la distancia de Manhattan como heurística para estimar la distancia del estado actual al estado final. La distancia de Manhattan es la suma de las distancias horizontales y verticales de cada ficha a su posición final.

                El algoritmo comienza con un límite igual a la distancia de Manhattan del estado inicial al estado final. Luego, se expande el estado actual y se calcula la distancia de Manhattan de cada vecino. Si la suma de la distancia del vecino y la longitud del camino actual es menor o igual al límite, se agrega el vecino al camino. Si la suma es mayor que el límite, se actualiza el límite con el valor mínimo de esta suma.

                El proceso se repite hasta que se alcanza el estado final o se agota el espacio de búsqueda. Cuando se encuentra la solución, el código imprime la secuencia de movimientos que lleva del estado inicial al estado final.
        '''
