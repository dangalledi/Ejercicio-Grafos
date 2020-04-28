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
            grafo.etiquetado.data = False
            setattr(grafo,'vertices',int(grafo.nodos.data))  
            print ("cantidad de vertices del grafo:",getattr(grafo,'vertices'))
            return render_template("grafo.html", nodes = getattr(grafo,'vertices'), type = grafo.tipo.data, name = grafo.nombre.data, labels = grafo.nodos.data, labeled = grafo.etiquetado.data)
        else:
            etiquetas = grafo.nodos.data.split(',') # de no ser dígitos lo toma como etiquetas y cantidad de nodos
            grafo.etiquetado.data = True
            print ("nodos etiquetados:",etiquetas)
            setattr(grafo,'vertices',len(etiquetas))
            print ("cantidad de vertices del grafo:",getattr(grafo,'vertices'))
            return render_template("grafo.html", nodes = getattr(grafo,'vertices'), type = grafo.tipo.data, name = grafo.nombre.data, labels = grafo.nodos.data, labeled = grafo.etiquetado.data)
    return render_template("tarea1.html", grafo = grafo)

@app.route('/graph/<int:nodes>/<string:type>/<string:name>/<string:labels>/<int:labeled>')
def graph(nodes,type,name,labels,labeled):
    #G = nx.complete_graph(nodes)
    G = nx.Graph()
    etiquetas = labels.split(',')
    dic_etiquetas = { i : etiquetas[i] for i in range(len(etiquetas))}   
    print(dic_etiquetas.items())
    for i in range(nodes):
        G.add_node(i)
        print(G.nodes())
    pos = nx.spring_layout(G)
    if labeled == False:
        nx.draw(G,with_labels=True)
    else:
        nx.draw_networkx_labels(G,pos,dic_etiquetas,font_size=11)
    img = BytesIO() # file-like object for the image
    plt.savefig(img) # save the image to the stream
    img.seek(0) # writing moved the cursor to the end of the file, reset
    plt.clf() # clear pyplot

    return send_file(img, mimetype = 'image/png')

#Se inicializa el servidor
if __name__=='__main__':
    app.run(debug=True)