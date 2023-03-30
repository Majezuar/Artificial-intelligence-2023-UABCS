'''
Hecho por Manuel Zúñiga
'''
import time,random
start_time = time.time()

def dfs_permutations(lst, path=[], goal=[]):
    if not goal:
        goal = sorted(lst)
    if len(lst) == len(path):
        if path == goal:
            return path
        else:
            return None
    for i in range(len(lst)):
        if lst[i] not in path:
            res = dfs_permutations(lst, path + [lst[i]], goal)
            if res:
                return res
#letras = ['z', 'y', 'x', 'w', 'v', 'u', 't', 's', 'r', 'q']  #CASO EXTREMO
letras = ['d', 'b', 'c', 'a']
goal = sorted(letras)
print("Lista inicial: ", letras, "\n")

res = dfs_permutations(letras, goal=goal)

if res:
    print("Elemento encontrado: ", res)
else:
    print("Elemento no encontrado")


end_time = time.time()
execution_time = end_time - start_time
print("El programa tardó {:.2f} segundos en ejecutarse.".format(execution_time))

