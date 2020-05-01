from flask import Flask, render_template, request, url_for, redirect, send_file
from forms import ClaseGrafo
from config import Config
from tareas.tarea1 import ingresa_grafo , muestra_datos

#Librerias para los grafos
import matplotlib
import matplotlib.pyplot as plt
from io import BytesIO
import networkx as nx

app = Flask(__name__)
app.config.from_object(Config)

# Ruta home 
@app.route('/')   
def home():
    return render_template('home.html')

# Ruta tarea 1 
@app.route('/tarea1', methods = ['GET', 'POST'])      
def tarea1():
    grafo = ClaseGrafo(request.form)      # se guardan los datos obtenidos del formulario  
    error = ""
    if request.method == 'POST':
        #Estos son todos los datos que me da el formulario

        print ("tipo de grafo:",grafo.tipo.data)
        print ("vertices:",grafo.vertices.data)
        print ("aristas:",grafo.aristas.data)

        if len(grafo.vertices.data) == 0 or len(grafo.aristas.data) ==0:
            error = "Por favor complete los campos"
        else:
            return render_template("grafo.html", types = grafo.tipo.data, nodes = grafo.vertices.data, edges = grafo.aristas.data)

    return render_template("tarea1.html", grafo = grafo, message=error)


@app.route('/graph/<string:types>/<string:nodes>/<string:edges>')
def graph(types,nodes,edges):

    if types == 'simple':  #Se crea Grafo
        G = nx.Graph()  # como grafo simple 
    else:
        G = nx.DiGraph()   #como digrafo

    G = ingresa_grafo(nodes,edges,G)     # se agregan los datos al grafo

    muestra_datos(G)    # Muestra los datos por consola
    nx.draw_networkx(G)     # Dibuja el grafo 
    img = BytesIO()     # guardando el objeto como imagen
    plt.savefig(img)    # guarda la imagen en la secuencia
    img.seek(0)     # la escritura movió el cursor al final del archivo, reset
    plt.clf()   # se limpia pyplot
#   G.clear()   # Se limpia el grafo

    return send_file(img, mimetype = 'image/png')

#Se inicializa el servidor
if __name__=='__main__':
    app.run(debug=True)