#import numpy as np


lista = [(0,1,3), (0,2,2), (2,3,5), (2,4,3), (3,5,2), (3,6,1)]
origen = 0
destino = 5
nodos = 7

def dijkstra(lista,origen,destino):
    
    nodos1 = [x[0] for x in lista]
    nodos2 = [y[1] for y in lista]
    pesos = [z[2] for z in lista]
    adyacentes = []
    camino = []
    acumulado = 0
    iteraciones = 0
    
    actual = origen
    while actual != destino:
        adyacentes.clear()
        for i in range(len(nodos1)):
            if nodos1[i] == actual:
                vecino = nodos2[i]
                adyacentes.append((actual,vecino,acumulado+pesos[i]))
                pesos_actuales = [p[2] in adyacentes for p in adyacentes]
                peso_min = min(pesos_actuales)
                for sig in adyacentes:
                    if sig[2] == peso_min:
                        actual = sig[1]
                        acumulado = acumulado + sig[2]
                        iteraciones = iteraciones + 1 
                        camino.append(sig[1])
    print(camino)
    return camino

    #print(filas)
    #print(columnas)
    #for i in columnas:
        #for j in filas:
                #adyacente[i][j] = 1
    #for i in range(len(columnas)):
        #for j in range(len(filas)):
            
    #print(adyacente[i][j])

#dijkstra(lista,origen,destino)
