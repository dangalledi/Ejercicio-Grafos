from collections import defaultdict
import numpy as np

auz = []

# EDGESYPESOS = [(0,1,16),(0,2,13),(1,2,10),(2,1,4),(1,3,12),(2,4,14),(3,2,9),(4,3,7),(3,5,20),(4,5,4)]

def creacion_matriz(matriz,n,iteracion): #retorna un arreglo n
    aux = np.zeros(n)
    for i in matriz:
        if i[0]==iteracion:
            k = i[1]
            aux[k] = i[2]
    return aux

def fix_arreglo(n,A):
    for i in range(n):
        lx = creacion_matriz(A,n,i) #matriz,cantidad nodos, iteracion
        auz.append(lx)
    return(auz)

class Graph:

	def __init__(self,graph): 
		self.graph = graph 
		self. ROW = len(graph) 

	def BFS(self,s, t, pariente): 

		visitado =[False]*(self.ROW) 
		queue=[] 
		queue.append(s) 
		visitado[s] = True
		while queue: 
			u = queue.pop(0) 
			for ind, val in enumerate(self.graph[u]): 
				if visitado[ind] == False and val > 0 : 
					queue.append(ind) 
					visitado[ind] = True
					pariente[ind] = u 
		return True if visitado[t] else False
			
	def algoritmo_FM(self, origen, destino): 
		pariente = [-1]*(self.ROW) 
		flujo_maximo = 0
		while self.BFS(origen, destino, pariente) : 
			camino_del_flujo = float("Inf") 
			s = destino 
			while(s != origen): 
				camino_del_flujo = min (camino_del_flujo, self.graph[pariente[s]][s]) 
				s = pariente[s] 
			flujo_maximo += camino_del_flujo 
			v = destino 
			while(v != origen): 
				u = pariente[v] 
				self.graph[u][v] -= camino_del_flujo 
				self.graph[v][u] += camino_del_flujo 
				v = pariente[v] 
		return flujo_maximo 



#como queda luego de pasar por fix_arreglo
# graph = [[0, 16, 13, 0, 0, 0], 
# 		[0, 0, 10, 12, 0, 0], 
# 		[0, 4, 0, 0, 14, 0], 
# 		[0, 0, 9, 0, 0, 20], 
# 		[0, 0, 0, 7, 0, 4], 
# 		[0, 0, 0, 0, 0, 0]] 

# aa = fix_arreglo(6,EDGESYPESOS)
# g = Graph(aa) 

# origen = 0; destino = 5

# print ("El flujo maximo posible es %d " % g.algoritmo_FM(origen, destino)) 


