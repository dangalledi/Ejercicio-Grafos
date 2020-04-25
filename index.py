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
    grafo = ClaseGrafo(request.form)# se guardan los datos obtenidos del formulario
    if request.method == 'POST':
        print("nombre del grafo:",grafo.nombre.data)
        #print ("eitquetado:",grafo.etiquetado.data)
        print ("tipo de grafo:",grafo.tipo.data)
        if  (grafo.nodos.data).isdigit() == True: #grafo.etiquetado.data == False and# de ser dígitos lo toma como la cantidad de nodos
            setattr(grafo,'vertices',int(grafo.nodos.data))  
            return render_template("grafo.html", nodes = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data)
        else:
            nodos = grafo.nodos.data.split(',') # de no ser dígitos lo toma como etiquetas y cantidad de nodos
            print ("nodos etiquetados:",nodos)
            setattr(grafo,'vertices',len(nodos))
            print ("cantidad de vertices del grafo:",getattr(grafo,'vertices'))
            return render_template("grafo.html", nodes = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data)
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