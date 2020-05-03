from queue import Queue #Libreria para colas
import numpy as np

G=[(1,2,3),(1,4,5),(2,3,2),(2,5,1),(5,4,3)] #Grafo Conexo
G2=[(1,2,5),(2,3,7),(4,5,7)] #Grafo No Conexo
nodos=5

def Conexo(s,M,n):
    visitado=np.zeros(n) #arreglo de ceros, cambia a 1 si es visitado
    cola = Queue()
    cola.put(s)
    visitado[s]=1
    while not cola.empty():
        s = cola.get()
        for i in range(nodos):
            if(visitado[i]==0):
                if (M[s][i]==1):
                    cola.put(i)
                    visitado[i] = 1
    total=0
    for j in range(len(visitado)):
        total = total + visitado[j]
    if total == n: 
        print("El grafo es conexo")
    else: 
        print("El Grafo no es conexo")

def Matriz(grafo,n):
    ma = np.zeros((n,n))
    for i in range(len(grafo)): 
        a=grafo[i][0]
        b=grafo[i][1]
        ma[a-1][b-1]=1
        ma[b-1][a-1]=1
    Conexo(0,ma,n)

Matriz(G2,nodos)