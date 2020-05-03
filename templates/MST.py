# Implementación del algoritmo Kruskal


from networkx.classes import graph
from networkx.algorithms.tree import mst #Algorimo para calcular los min/max
from operator import itemgetter #proporciona funciones para hacer que las 
                                #funciones de acceso sean más fáciles y rápidas, al buscar en las listas.

# Variables globales
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

    # A = {conjunto vacío}
    mst = set()
   
    # Para todo vértice v en G.V
    for v in graph['vertices']:
        generar_conjuntos(v)
    print ("Sub gráficos creados:")
    print (base)

    # Ordena la lista G.A en forma no decendente por su peso w
    # En este caso usamos el ordenador dentro de python
    Aristas = list(graph['Aristas'])

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
            mst.add(e)
    return mst 

graph={
'vertices': [1,2,3,4,5,6],
'Aristas': set([
    (1,3,5),
    (1,4,3),
    (2,4,2),
    (3,4,1),
    (6,4,5),
    (2,6,3),
    (6,5,6),
    (1,2,5),
    (2,1,1)])
    
    }


k = kruskal(graph)
print ("Resultado MST:")
print (k)