import networkx as nx # librería para usar grafos
import matplotlib.pyplot as plt # librería para dibujar

# Se define un grafo con sus respectivos nodos y aristas
G = nx.Graph()
V=[1,2,3,4,5]
E=[(1,2),(3,4),(2,4),(3,5),(3,1)]

G.add_nodes_from(V) #nodos
G.add_edges_from(E) #Aristas

# ver cantidad de nodos y aristas
print('Cantidad de nodos:',G.number_of_nodes())
print('Cantidad de aristas:',G.number_of_edges())

# Ver nodos y aristas del grafo
print('Nodos: \n',list(G.nodes))   # ver nodos
print('Aristas: \n',list(G.edges)) # ver aristas


nx.draw_networkx(G) 

plt.show()  # mostrar dibujo}
