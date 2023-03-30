'''
Hecho por Manuel Zúñiga
'''
import time,random
from collections import deque
start_time = time.time()

def bfs_permutations(lst, goal=[]):
    if not goal:
        goal = sorted(lst)
    queue = deque([[i] for i in lst])
    while queue:
        path = queue.popleft()
        if len(path) == len(lst):
            if path == goal:
                return path
            else:
                continue
        for i in lst:
            if i not in path:
                queue.append(path + [i])
    return None

#  ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q']  #CASO EXTREMO
letras = ['d', 'b', 'c', 'a']
goal = sorted(letras)

print("Lista inicial: ", letras, "\n")

res = bfs_permutations(letras, goal)

if res:
    print("Elemento encontrado: ", res)
else:
    print("Elemento no encontrado")
      
end_time = time.time()
execution_time = end_time - start_time
print("El programa tardó {:.2f} segundos en ejecutarse.".format(execution_time))




