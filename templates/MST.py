# Implementación del algoritmo Kruskal


from networkx.classes import graph
from networkx.algorithms.tree import mst #Algorimo para calcular los min/max

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

    # Ordena la lista G.E en forma no decendente por su peso w
    # En este caso usamos el ordenador dentro de python
    Aristas = list(graph['Aristas'])
    Aristas.sort()
    
    print ("Aristas ordenadas:")
    print (Aristas)

    # Para toda arista(u,v) en G.E
    for e in Aristas:
        weight, u, v = e
        if Buscar(u) != Buscar(v):
            # A = A union (u,v)
            union(u, v)
            # Union(u,v)
            mst.add(e)
    return mst 

graph={
'vertices': ['a','b','c','d','e','f'],
'Aristas': set([
    (5,'a','c'),
    (3,'a','d'),
    (2,'b','d'),
    (1,'c','d'),
    (5,'f','d'),
    (3,'b','f'),
    (6,'f','e'),
    (1,'a','b'),
    (1,'f','b')
    ])
}

k = kruskal(graph)
print ("Resultado MST:")
print (k)