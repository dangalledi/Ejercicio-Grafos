from queue import Queue #Libreria para colas
import numpy as np #Libreria para la matriz

#Ejemplo
G=[(1,2,3),(1,4,5),(2,3,2),(2,5,1),(5,4,3)] #Grafo Conexo
G2=[(1,2,5),(2,3,7),(4,5,7)] #Grafo No Conexo
nodos=5

matriz = np.zeros((nodos,nodos)) #Creo una matriz de ceros
def Matriz(grafo,n):
    aux = np.zeros((n,n))
    for i in range(len(grafo)): 
        a=grafo[i][0]
        b=grafo[i][1]
        aux[a-1][b-1]=1
        aux[b-1][a-1]=1
    return aux

def BFS(s,M,n):
    visitado=np.zeros(n) #arreglo de ceros, cambia a 1 si es visitado
    cola = Queue()
    cola.put(s)
    visitado[s]=1
    while not cola.empty():
        s = cola.get()
        for i in range(nodos):
            if (M[s][i]==1):
                cola.put(i)
                visitado[i] = 1
    return visitado

matriz=Matriz(G2,nodos)
print(matriz)
visit = BFS(0,matriz,nodos)
print(visit)

#Matriz
#    0 1 2 3 4
#0   0 1 0 1 0   1
#1   1 0 1 0 1   2
#2   0 1 0 0 0   3
#3   1 0 0 0 1   4 
#4   0 1 0 1 0   5