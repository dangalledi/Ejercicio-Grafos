from flask import Flask, render_template, request, url_for, redirect, send_file
from forms import ClaseGrafo
from config import Config
from tareas.tarea1 import ingresa_grafo

#Librerias para los grafos
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import networkx as nx

app = Flask(__name__)
app.config.from_object(Config)

grafos = []

# Ruta home 
@app.route('/')   
def home():
    return render_template('home.html')

# Ruta tarea 1 
@app.route('/tarea1', methods = ['GET', 'POST'])      
def tarea1():
    grafo = ClaseGrafo(request.form)      # se guardan los datos obtenidos del formulario  
    aux1 = grafo.nodos
    aux2 = str(aux1)
    nodos = []
    nodos = aux2.split(',')
    if request.method == 'POST':
        #print (grafo.vertices.data)
        print (grafo.tipo.data)
        print (grafo.etiquetado.data)
        #grafos=[grafo.vertices.data,grafo.aristas.data]
        #print (grafos)
        print(grafo.nombre.data)
        print (nodos)
        print (len(nodos))
        return render_template("grafo.html", nodes = len(nodos), tipo = grafo.tipo.data, nombre = grafo.nombre.data)

    return render_template("tarea1.html", grafo = grafo)


@app.route('/graph/<int:nodes><string:nombre><string:tipo>')
def graph(nodes,tipo,nombre):
    G = nx.complete_graph(nodes)
    nx.draw(G)
    img = BytesIO() # file-like object for the image
    plt.savefig(img) # save the image to the stream
    img.seek(0) # writing moved the cursor to the end of the file, reset
    plt.clf() # clear pyplot

    return send_file(img, mimetype = 'image/png')

#Se inicializa el servidor
if __name__=='__main__':
    app.run(debug=True)