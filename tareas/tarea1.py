import networkx as nx # librería para usar grafos

def ingresa_grafo (vertices , aristas , grafo):

    for i in range (len(aristas)):
        if ( '(' == aristas[i]): 
            grafo.add_edge(aristas[i+1] , aristas[i+3])

    i=0
    grafo.add_node(vertices[i])
    for i in range (len(vertices)):
        if ( ',' == vertices[i]): 
            grafo.add_node(vertices[i+1])

    return grafo
    
def muestra_datos (grafo):

    # ver cantidad de nodos y aristas
    print('Cantidad de nodos:',grafo.number_of_nodes())
    print('Cantidad de aristas:',grafo.number_of_edges())

    # Ver nodos y aristas del grafo
    print('Nodos: \n',list(grafo.nodes))   # ver nodos
    print('Aristas: \n',list(grafo.edges)) # ver aristas

    return 