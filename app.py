from flask import Flask, render_template, request, url_for, redirect, send_file
from forms import ClaseGrafo, PostForm
from config import Config

#Librerias para los grafos
import matplotlib
matplotlib.use('Agg')
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
    grafo = ClaseGrafo()            # cada vez que ingresa a la función de la ruta se crea el objeto grafo con los inputs
    form = PostForm()           # 2do form realizar tareas con el grafo
    if request.method == 'POST':            # if de request ya hecho
        if ((form.origen.data,form.destino.data,form.peso.data)) not in getattr(grafo,'aristas') and form.tarea.data == 'agregar':
            grafo.aristas.append((int(form.origen.data),int(form.destino.data),float(form.peso.data)))            # si el primer caracter del string es dígito lo agrega como vector a aristas
            # al estar vacío el atributo aristas, la 1era vez toma la N de None y no se pueden repetir 
        
        elif form.tarea.data == 'corto':
            print("¡¡¡   IMPLEMENTAR ALGORITMO DE DJISKTRA   !!!")            # ¡¡¡IMPLEMENTAR ALGORITMO DE DJISKTRA!!!
        
        elif form.tarea.data == 'flujo':
            print("¡¡¡   IMPLEMENTAR FLUJO MÁXIMO   !!!")         #¡¡¡IMPLEMENTAR FLUJO MÁXIMO!!!

        else:
            setattr(grafo,'aristas',[])
            setattr(grafo,'vertices',0)

        print("nombre del grafo:",grafo.nombre.data)            # print de consola ¡¡¡ AÑADIR CONDICIÓN DE NOMBRE NO NUMÉRICO !!!
        print("eitquetado:",grafo.etiquetado.data)          # print de consola
        print("tipo de grafo:",grafo.tipo.data)         # print de consola
        print("nodos seleccionados para tarea (n°: origen, destino): ("+form.origen.data+", "+form.destino.data+")")         # print de consola
        print("Aristas del grafo: ",getattr(grafo,"aristas"))
        
        grafo.nombre.data = grafo.nombre.data.replace(' ','')
        if  (grafo.nodos.data).isdigit() == True:           # if de si el ingreso son solo números implicitamente se deduce grafo no etiquetado
            grafo.etiquetado.data = False           # atributo booleano etiquetado del grafo se hace falso
            form.origen.choices = [(i,str(i)) for i in range(int(grafo.nodos.data))]          # se ingresan las opciones dinámicas al atributo origen
            form.destino.choices = [(i,str(i)) for i in range(int(grafo.nodos.data))]         # se ingresan las opciones dinámicas al atributo destino
            setattr(grafo,'vertices',int(grafo.nodos.data))         # como la data es string se tiene que convertir a entero y obtener la cantidad de nodos/vertices 
            
            print("cantidad de vertices del grafo:",getattr(grafo,'vertices'))          # print de consola
        
        else:
            grafo.nodos.data = grafo.nodos.data.replace(' ','')
            etiquetas = grafo.nodos.data.split(',')         # de no ser dígitos lo toma como etiquetas y cantidad de nodos
            grafo.etiquetado.data = True            # if de si el ingreso es una lista implicitamente se deduce grafo etiquetado
            form.origen.choices = [(i,str(i)+": "+etiquetas[i]) for i in range(len(etiquetas))]         # la otra manera si es un nodo etiquetado
            form.destino.choices = [(i,str(i)+": "+etiquetas[i]) for i in range(len(etiquetas))]        # la otra manera si es un nodo etiquetado
            setattr(grafo,'vertices',len(etiquetas))            # se le asigna al atributo vertices del grafo el largo de la lista
            
            print("nodos etiquetados:",etiquetas)           # print de consola
            print("cantidad de vertices del grafo:",getattr(grafo,'vertices'))          # print de consola
        
        return render_template("grafo.html", grafo = grafo, form = form, nodos = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data, etiquetas = grafo.nodos.data, etiquetado = grafo.etiquetado.data, aristas = getattr(grafo,'aristas'))
        # se retorna a la misma función el template grafo.html con la función render_template() que sobrepone el html sobre tarea1.html sin cambiar la ruta (Flask)
    
    return render_template("tarea1.html", grafo = grafo)

@app.route('/graph/<int:nodos>/<string:tipo>/<string:nombre>/<string:etiquetas>/<int:etiquetado>/<string:aristas>') # se usa una ruta que contiene los datos del grafo para que Flask los compile
def grafica(nodos,tipo,nombre,etiquetas,etiquetado,aristas):
    if tipo == 'simple':            # si el atributo tipo es la constante 'simple' se crea el objeto grafo G sin direcciones
        G = nx.Graph()
    else:
        G = nx.DiGraph()            # si el atributo es la constante 'direccionado' se crea el objeto grafo G direccionado
    if etiquetado == True:
        labels = etiquetas.split(',')
        dic_etiquetas = { i : labels[i] for i in range(len(labels))}
        print("-------------------------------------------------------",dic_etiquetas.items())            # print de consola
        G.add_nodes_from(labels) 
    else:
        for i in range(nodos):
            G.add_node(i)
    #print(G.nodes())            # print de consola
    nx.draw(G,with_labels=True)
    img = BytesIO()         # se le asigna memoria a la imagen
    plt.savefig(img)            # se guarda la imagen del stream al objeto plt que creará la imagen
    img.seek(0)         # 
    plt.clf()           # limpia el caché del graficado

    return send_file(img, mimetype = 'image/png') # retorna la imagen que se agrega al html mediante a send_file() función de Flask

#Se inicializa el servidor
if __name__=='__main__':
    app.run(debug=True)