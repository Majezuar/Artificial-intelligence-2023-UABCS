'''
Hecho por Manuel Zúñiga
'''
import time,random
from collections import deque
start_time = time.time()

def dfs_permutations(lst, goal):
    stack = [(lst, [])]
    while stack:
        node, path = stack.pop()
        if path == goal:
            return path
        for i in range(len(node)):
            if node[i] not in path:
                stack.append((node[:i] + node[i+1:], path + [node[i]]))
    return None


letras = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q']  #CASO EXTREMO
letras = ['d', 'b', 'c', 'a']
goal = sorted(letras)
print("Lista inicial: ", letras, "\n")

res = dfs_permutations(letras, goal=goal)

if res:
    print("Elemento encontrado:", res)
    
else:
    print("Elemento no encontrado")


end_time = time.time()
execution_time = end_time - start_time
print("El programa tardó {:.2f} segundos en ejecutarse.".format(execution_time))


