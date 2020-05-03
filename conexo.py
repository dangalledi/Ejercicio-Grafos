from collections import deque #Libreria para colas
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