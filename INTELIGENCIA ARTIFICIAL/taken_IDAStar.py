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
