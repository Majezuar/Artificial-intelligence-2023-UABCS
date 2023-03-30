'''
Hecho por Manuel Zúñiga
'''
import time,random
from collections import deque
start_time = time.time()

def ida_star_permutations(lst, goal):
    def h(node):
        # Heurística consistente
        return sum(hamming(a, b) for a, b in zip(node, goal))

    def hamming(a, b):
        # Distancia de Hamming entre dos elementos
        return int(a != b)

    letras = tuple(lst)
    goal = tuple(goal)
    threshold = h(letras)
    while True:
        next_threshold = float('inf')
        visited = {letras: 0}
        stack = [(h(letras), letras)]
        while stack:
            f, node = stack.pop()
            if node == goal:
                return node
            if f > threshold:
                next_threshold = min(next_threshold, f)
            else:
                for i in range(len(node)):
                    for j in range(i + 1, len(node)):
                        # Genera todos los posibles siguientes estados a partir de los intercambios de dos elementos
                        next_node = node[:i] + (node[j],) + node[i+1:j] + (node[i],) + node[j+1:]
                        g = visited[node] + 1
                        if next_node not in visited or g < visited[next_node]:
                            visited[next_node] = g
                            stack.append((g + h(next_node), next_node))
        if next_threshold == float('inf'):
            return None
        threshold = next_threshold
#letras = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q']  #CASO EXTREMO
letras = ['d', 'b', 'c', 'a']
goal = sorted(letras)

print("Lista inicial: ", letras)

res = ida_star_permutations(letras, goal=goal)

if res is not None:
    print("Elemento encontrado:", res)
else:
    print("Elemento no encontrado")



end_time = time.time()
execution_time = end_time - start_time
print("El programa tardó {:.2f} segundos en ejecutarse.".format(execution_time))