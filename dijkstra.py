import sys

# Function to find out which of the unvisited node 
# needs to be visited next
def avisitar():
  global visitado_distancia
  v = -10
  # Choosing the vertex with the minimum distance
  for index in range(number_of_vertices):
    if visitado_distancia[index][0] == 0 \
      and (v < 0 or visitado_distancia[index][1] <= \
      visitado_distancia[v][1]):
        v = index
  return v

# Creating the graph as an adjacency matrix
vertices = [[0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
            [0, 0, 0, 0]]
edges =  [[0, 3, 4, 0],
          [0, 0, 0.5, 0],
          [0, 0, 0, 1],
          [0, 0, 0, 0]]

number_of_vertices = len(vertices[0])

# The first element of the lists inside visited_and_distance 
# denotes if the vertex has been visited.
# The second element of the lists inside the visited_and_distance 
# denotes the distance from the source.
visitado_distancia = [[0, 0]]
for i in range(number_of_vertices-1):
  visitado_distancia.append([0, sys.maxsize])

for vertex in range(number_of_vertices):
  # Finding the next vertex to be visited.
  visitar = avisitar()
  for index_vecino in range(number_of_vertices):
    # Calculating the new distance for all unvisited neighbours
    # of the chosen vertex.
    if vertices[visitar][index_vecino] == 1 and \
     visitado_distancia[index_vecino][0] == 0:
      new_distance = visitado_distancia[visitar][1] \
      + edges[visitar][index_vecino]
      # Updating the distance of the neighbor if its current distance
      # is greater than the distance that has just been calculated
      if visitado_distancia[index_vecino][1] > new_distance:
        visitado_distancia[index_vecino][1] = new_distance
    # Visiting the vertex found earlier
    visitado_distancia[visitar][0] = 1

i = 0 

# Printing out the shortest distance from the source to each vertex       
for distance in visitado_distancia:
  print("The shortest distance of ",chr(ord('a') + i),\
  " from the source vertex a is:",distance[1])
  i = i + 1
