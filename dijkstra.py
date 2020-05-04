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
    def operador(actual,acumulado,iteraciones): 
        if actual != destino:
            adyacentes.clear()
            for i in range(len(nodos1)):
                print("XDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDDD")
                if nodos1[i] == actual:
                    print("actual : ",actual)
                    input()
                    vecino = nodos2[i]
                    print("Vecino : ",vecino)
                    input()
                    adyacentes.append((actual,vecino,acumulado+pesos[i]))
                    pesos_actuales = [p[2] in adyacentes for p in adyacentes]
                    print(pesos_actuales)
                    input()
                    peso_min = min(pesos_actuales)
                    print("Peso mínimo: ",peso_min)
                    input()
                for sig in adyacentes:
                    print("sig actual : ",sig)
                    input()
                    if sig[2] == peso_min:
                        actual = sig[1]
                        print("actual + 1: ",actual)
                        input()
                        acumulado = acumulado + sig[2]
                        iteraciones = iteraciones + 1 
                        print("iteraciones: ",iteraciones)
                        input()
                        camino.append(sig[1])
                        print("camino hasta ahora : ",camino)
                        input()
                        return operador(actual)
        else:
            return actual
        camino.append(operador())
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
