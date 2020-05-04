from flask import Flask, render_template, request, url_for, redirect, send_file
from forms import ClaseGrafo, PostForm
from config import Config
from nwfixes import fix, fix2
from FlujoMaximo import Graph,fix_arreglo,creacion_matriz
from tarea1 import kruskal, Matriz, encontrar_camino_euleriano ,encontrar_camino_hamiltoniano ,es_euleriano_interrogacion_xD, cant_nodos
from dijkstra import dijkstra

#Librerias para los grafos
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import networkx as nx

app = Flask(__name__)
app.config.from_object(Config)
error = ''

# Ruta home 
@app.route('/')   
def home():
    return render_template('pre-load.html')

# Ruta tarea 1 
@app.route('/tarea1', methods = ['GET', 'POST'])      
def tarea1():
    grafo = ClaseGrafo()            # cada vez que ingresa a la función de la ruta se crea el objeto grafo con los inputs
    form = PostForm()           # 2do form realizar tareas con el grafo
    error = ''
    if request.method == 'POST':
        
        
        
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

        if  form.tarea.data == 'agregar' and form.destino.data[0].isdigit() == True and ((int(form.origen.data),int(form.destino.data),float(form.peso.data))) not in getattr(grafo,'aristas'):
            grafo.vectores.append((int(form.origen.data),int(form.destino.data)))
            grafo.aristas.append((int(form.origen.data),int(form.destino.data),float(form.peso.data)))            # si el primer caracter del string es dígito lo agrega como vector a aristas
            # al estar vacío el atributo aristas, la 1era vez toma la N de None y no se pueden repetir
        
        elif form.tarea.data == 'corto':
            print("El camino más corto es: ",dijkstra(getattr(grafo,'aristas'),int(form.origen.data),int(form.destino.data)))

        elif form.tarea.data == 'flujo':
            cantidad_nodos = getattr(grafo,'vertices') #cantidad de nodos !!!
            matriz_tal_por_cual = getattr(grafo,'aristas')  #[nodo,nodo,peso] !!!
            print(cantidad_nodos)
            print(matriz_tal_por_cual)
            origen_nodo = int(form.origen.data)#ok
            destino_nodo = int(form.destino.data) #ok
            print(origen_nodo,destino_nodo)
            fix_grafo = fix_arreglo(cantidad_nodos,matriz_tal_por_cual)#ok
            print(fix_grafo)#ok
            g = Graph(fix_grafo)#ok
            result = g.algoritmo_FM(origen_nodo,destino_nodo)#ok
            print ("Flujo Maximo /////////////////////////////////////",result)#ok
            fix_grafo.clear()
            return render_template("grafo.html", grafo = grafo, form = form, nodos = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data, etiquetas = grafo.nodos.data, etiquetado = grafo.etiquetado.data, vectores = getattr(grafo,'vectores'),resultado= result)
#######################################################################################################################

        elif form.tarea.data == 'hamiltoniano':
            aristas=getattr(grafo,'aristas') #Aristas tipo (int,int,float)
            hamiltoniano = encontrar_camino_hamiltoniano( aristas )
            if (hamiltoniano):
                print ('Camino Hamiltoniano: ', hamiltoniano) ## Retorna una lista 
                mensaje = 'El camino es :',hamiltoniano ,'siendo un grafo hamiltoniano'
                return render_template("grafo.html", grafo = grafo, form = form, nodos = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data, etiquetas = grafo.nodos.data, etiquetado = grafo.etiquetado.data, vectores = getattr(grafo,'vectores'),resultado= mensaje)
                

        elif form.tarea.data == 'euleriano':
            aristas=getattr(grafo,'aristas') #Aristas tipo (int,int,float)
            euleriano = es_euleriano_interrogacion_xD( aristas )
            if ( type(euleriano) != False ):   
                camino = encontrar_camino_euleriano(aristas)
                print ('Grafo euleriano: ', euleriano)
                print ('Camino euleriano: ', camino)
                mensaje = 'El camino es :',camino ,'siendo un grafo euleriano'
                return render_template("grafo.html", grafo = grafo, form = form, nodos = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data, etiquetas = grafo.nodos.data, etiquetado = grafo.etiquetado.data, vectores = getattr(grafo,'vectores'),resultado= mensaje)
                # se retorna a la misma función el template grafo.html con la función render_template() que sobrepone el html sobre tarea1.html sin cambiar la ruta (Flask)

        elif (form.tarea.data == 'conexo'): #Funcion si es conexo o no conexo
            G=getattr(grafo,'aristas') #Aristas tipo (int,int,float)
            N=cant_nodos(G)+1 #Cantidad de nodos
            Matriz(G, N)  #Implementacion conexo

        elif form.tarea.data == 'arbol': 

            #Si lo que entra es el numero de nodos
            if(grafo.nodos.data).isdigit() == True:
                Vertices = []
                for i in range (int(grafo.nodos.data)):
                    Vertices.append(i)

                Ar=kruskal(Vertices,getattr(grafo,'aristas'))
                #Print de consola
                print ("El resultado de la MTS:",Ar) 
                #impresion del resultado en la pagina
                return render_template("grafo.html", grafo = grafo, form = form, nodos = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data, etiquetas = grafo.nodos.data, etiquetado = grafo.etiquetado.data, vectores = getattr(grafo,'vectores'),resultado= Ar)

            #Si lo que entra es una lista de etiquetas
            else:
                AristasNuevas = grafo.nodos.data 
                Vertices = []
                for i in range (len(AristasNuevas)):
                    Vertices.append(i)
                Ar=kruskal(Vertices,getattr(grafo,'aristas'))
                #Print de consola
                print ("El resultado de la MTS:",Ar)
                #impresion del resultado en la pagina
                return render_template("grafo.html", grafo = grafo, form = form, nodos = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data, etiquetas = grafo.nodos.data, etiquetado = grafo.etiquetado.data, vectores = getattr(grafo,'vectores'),resultado= Ar)

        elif form.tarea.data == 'actualizar':
            grafo.vectores.clear()
            grafo.aristas.clear()
            setattr(grafo,'vertices',0)

        print("nombre del grafo:",grafo.nombre.data)            # print de consola ¡¡¡ AÑADIR CONDICIÓN DE NOMBRE NO NUMÉRICO !!!
        print("eitquetado:",grafo.etiquetado.data)          # print de consola
        print("tipo de grafo:",grafo.tipo.data)         # print de consola
        print("nodos seleccionados para tarea (n°: origen, destino): ("+form.origen.data+", "+form.destino.data+")")         # print de consola
        print("vectores $$$$$$$$$$$$$$$$$$$ = : ",getattr(grafo,"vectores"))
        
        if grafo.nodos.data == '' or grafo.nombre.data == '':
            error = "estos campos no pueden quedar vacíos :/"
            return render_template("tarea1.html", grafo = grafo, message = error)
        
        if isinstance(form.peso.data, float) == False and form.origen.data != 'None':
            error = "El peso debe ser un numérico decimal"
            return render_template("grafo.html", grafo = grafo, form = form, nodos = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data, etiquetas = grafo.nodos.data, etiquetado = grafo.etiquetado.data, vectores = getattr(grafo,'vectores'), message = error)

        return render_template("grafo.html", grafo = grafo, form = form, nodos = getattr(grafo,'vertices'), tipo = grafo.tipo.data, nombre = grafo.nombre.data, etiquetas = grafo.nodos.data, etiquetado = grafo.etiquetado.data, vectores = getattr(grafo,'vectores'))
        # se retorna a la misma función el template grafo.html con la función render_template() que sobrepone el html sobre tarea1.html sin cambiar la ruta (Flask)
    
    return render_template("tarea1.html", grafo = grafo)

@app.route('/graph/<int:nodos>/<string:tipo>/<string:nombre>/<string:etiquetas>/<int:etiquetado>/<string:vectores>') # se usa una ruta que contiene los datos del grafo para que Flask los compile
def grafica(nodos,tipo,nombre,etiquetas,etiquetado,vectores):

    if tipo == 'simple':            # si el atributo tipo es la constante 'simple' se crea el objeto grafo G sin direcciones
        G = nx.Graph()
    else:
        G = nx.DiGraph()            # si el atributo es la constante 'direccionado' se crea el objeto grafo G direccionado
    if etiquetado == True:
        labels = etiquetas.split(',')
        dic_etiquetas = { i : labels[i] for i in range(len(labels))}
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$",dic_etiquetas.items())            # print de consola
        G.add_nodes_from(labels)
    else:
        for i in range(nodos):
            G.add_node(i)

    if vectores != "[]" and etiquetado==True:
        j = fix(vectores,dic_etiquetas)
        G.add_edges_from(j)

    if vectores != "[]" and etiquetado==False:
        j = fix2(vectores)
        G.add_edges_from(j)


    #print(G.nodes())            # print de consola
    nx.draw_planar(G,with_labels=True)
    img = BytesIO()         # se le asigna memoria a la imagen
    plt.savefig(img)            # se guarda la imagen del stream al objeto plt que creará la imagen
    img.seek(0)         # 
    plt.clf()           # limpia el caché del graficado

    return send_file(img, mimetype = 'image/png') # retorna la imagen que se agrega al html mediante a send_file() función de Flask

#Se inicializa el servidor
if __name__=='__main__':
    app.run(debug=True)