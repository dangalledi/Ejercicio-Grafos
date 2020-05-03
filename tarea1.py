#Matriz de Camino --> Simple 
from operator import itemgetter

def matriz_de_adyacencia(nodos,aristas):
    MatrizCaminos = []
    for i in range(len(nodos)):
        MatrizCaminos.append([])
        for j in range(len(nodos)):
            MatrizCaminos[i].append(0)

    for c in aristas:
        for a in range(len(nodos)):
            for b in range(len(nodos)):
                if ((b+1 == int(c[0]) and a+1 ==int(c[1])) or (b+1 == int(c[1]) and a+1 == int(c[0]))):
                    MatrizCaminos[a][b]=MatrizCaminos[a][b]+1

    return MatrizCaminos

#Matriz de Camino --> Direccionada 
def matriz_de_adyacencia_direccionada(nodos,aristas):
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

def lista_de_grados_de_nodos(matriz):

    listaGrados = []
    for a in range(len(nodos)):                         
        aux = 0
        for b in range(len(nodos)):
            aux = aux+ matriz[a][b]
        listaGrados.append(aux)

    return listaGrados

def encontrar_camino_hamiltoniano(aristas,nodos):
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
    
    # Función principal del algoritmo Kruskal
def kruskal(graph):
    mst = set() #convierte a mst en un conjunto vacío
    # Para todo vértice v en G.V
    for v in graph['vertices']:
        generar_conjuntos(v)
    # Ordena la lista G.A en forma no decendente por su peso w
    # En este caso usamos el ordenador dentro de python
    Aristas = list(graph['Aristas']) #lo convierte nuevamente a lista para poder usar sort()
    Aristas.sort(key=itemgetter(2))
    print ("Aristas ordenadas:")
    print (Aristas)

    # Para toda arista(u,v) en G.A
    for e in Aristas:
        (u,v,peso)  = e
        if Buscar(u) != Buscar(v):
            # A = A union (u,v)
            union(u, v)
            # Union(u,v)
            mst.add(e) #se adhieren al conjunto msd el elemento e=(u,v,peso) generado
    return mst 
