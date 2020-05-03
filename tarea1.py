from operator import itemgetter
from queue import Queue #Libreria para colas
import numpy as np

def traductor (aristas):  #[(int,int,float),(int,int,float),...,(int,int,float)]

    aristas = np.array(aristas)
    if (aristas.ndim == 3):
        nodos = np.delete(aristas, 2, axis=1)   # [(int,int),(int,int),(int,int), ... ,(int,int)]
    else :
        return aristas   
                  
    return nodos

def matriz_de_adyacencia(nodos,aristas):
    MatrizCaminos = []
    for i in range(len(nodos)):
        MatrizCaminos.append([])
        for j in range(len(nodos)):
            MatrizCaminos[i].append(0)

    for c in aristas:
        for a in range(len(nodos)):
            for b in range(len(nodos)):
                if ((a+1 == int(c[0]) and b+1 ==int(c[1]))):
                    MatrizCaminos[a][b]=MatrizCaminos[a][b]+1

    return MatrizCaminos

def encontrar_camino_euleriano(aristas):
    camino = []

    vertice_actual = aristas[0][0]
    camino.append(vertice_actual)

    while len(aristas) > 0:
        print(aristas,vertice_actual)
        for i in aristas:
            if vertice_actual in i:
                if i[0] == vertice_actual:
                    vertice_actual = i[1]
                else:
                    vertice_actual = i[0]

                aristas.remove(i)
                camino.append(vertice_actual)
                break       
        else:
            print('No hay camino euleriano')
            return False
            
    return camino

def lista_de_grados_de_nodos(matriz,nodos):

    listaGrados = []
    for a in range(len(nodos)):                         
        aux = 0
        for b in range(len(nodos)):
            aux = aux+ matriz[a][b]
        listaGrados.append(aux)

    return listaGrados

def encontrar_camino_hamiltoniano(aristas,nodos):
    aristas = traductor(aristas)
    camino = []
    caminito =[]
    arista=[]
    for c in aristas:
        arista.append(c)
    
    vertice_actual = arista[0][0]
    camino.append(vertice_actual)
    for c in aristas:    
        for i in arista:
            if vertice_actual in i:
                if i[0] == vertice_actual:
                    vertice_actual = i[1]
                else:
                    vertice_actual = i[0]

                arista.remove(i)
                camino.append(vertice_actual)
    if (len(aristas)<2):
        print ('No es hamiltoniano')
        return False            
    if(len(camino)<(len(nodos))+1 ):
        for i in aristas:    
            if((i[0]== camino[int(len(camino)/2)] and i[1]== camino[int(len(camino)/2)-1]) or( i[0]== camino[int(len(camino)/2)-1] and i[1]== camino[int(len(camino)/2)])):
                aristas.remove(i)
                caminito =encontrar_camino_hamiltoniano(aristas,nodos)
                return caminito
    else:
        print ('Es hamiltoniano')
        return camino
        
    return caminito

#Implementacion de Kruskal

#Variables para Kruskal 
base = dict()
ord = dict()   

    # Función para generar conuntos
def generar_conjuntos(v):
    base[v] = v
    ord[v] = 0

# Implementación de la función de búsqueda 
# de manera recursiva
def Buscar(v):
    if base[v] != v:
        base[v] = Buscar(base[v])
    return base[v]

# Implementación de la unión de conjuntos
def union(u, v):
    v1 = Buscar(u)
    v2 = Buscar(v)
    if v1 != v2:
        if ord[v1] > ord[v2]:
            base[v2] = v1 
        else:
            base[v1] = v2
            if ord[v1] == ord[v2]: 
                ord[v2] += 1
    

def es_euleriano_interrogacion_xD (nodos,aristas):
    aristas = traductor(aristas)
    auxiliar= 0
    auxiliargrado = 0
    Matriz_Adyacencia = matriz_de_adyacencia(nodos,aristas)   
    for i in lista_de_grados_de_nodos(Matriz_Adyacencia,nodos):         
        if (i%2==0):
            auxiliar = auxiliar +1
        else:
            auxiliargrado = auxiliargrado + 1

    if(auxiliar != (len(nodos)) or encontrar_camino_euleriano == False):
        print('No es Euleriano')
        return False
    elif (auxiliargrado%2 == 0 and (auxiliar == (len(nodos))-auxiliargrado)):
        print ('Es Euleriano')
        return True
    else:
        print('Es Euleriano :)')
        return True
    return 0

    # Función principal del algoritmo Kruskal
def kruskal(graph):
    # A = {conjunto vacío}
    mst = set()
    # Para todo vértice v en G.V
    for v in graph['vertices']:
        generar_conjuntos(v)
    # Ordena la lista G.A en forma no decendente por su peso w
    # En este caso usamos el ordenador dentro de python
    Aristas = list(graph['Aristas'])
    Aristas.sort(key=itemgetter(2))
    # Para toda arista(u,v) en G.A
    for e in Aristas:
        (u,v,peso)  = e
        if Buscar(u) != Buscar(v):
            # A = A union (u,v)
            union(u, v)
            # Union(u,v)
            mst.add(e)
    return mst 

def Conexo(s,M,n):
    visitado=np.zeros(n) #arreglo de ceros, cambia a 1 si es visitado
    cola = Queue()
    cola.put(s)
    visitado[s]=1
    while not cola.empty():
        s = cola.get()
        for i in range(n):
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
    print(ma)
    Conexo(0,ma,n)