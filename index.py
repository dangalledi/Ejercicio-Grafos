from flask import Flask, render_template, request, url_for, redirect, send_file
from form import ClaseGrafo
import matplotlib
from config import Config
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import networkx as nx

app = Flask(__name__)
app.config.from_object(Config)

def procesado_formulario(d): #3. Metodo de recorte de arrglo
    print(d)
    print (len(d))
    if len(d)==5: # Si sus items son 5 se trata de un grafo dirigido, es este caso d=['D', 'NombreGrafos', '', '1,2;2,3;3,4;2,4;5,5;6,2', '1,2,3,4,5,6'] = [Dirigido,Nombre,nombres-nodos,edges,pesos]
        nuevo = []#No importa si el campo de nombres-nodos esta vacio, ya que igual genera un espacio contable.
        edges = d[3].split(";")
        pesos = d[4].split(",")
        for i in range(len(pesos)):
            a = tuple(edges[i].replace(",","")+pesos[i])
            print(a)
            nuevo.append(a)
        return nuevo # retorna [('1', '2', '1'), ('2', '3', '2'), ('3', '4', '3'), ('2', '4', '4'), ('5', '5', '5'), ('6', '2', '6')]
    else: #Menor a esto tenemos un grafo no dirigido
        nuevo = []
        edges = d[1].split(";")
        pesos = d[2].split(",")
        for i in range(len(pesos)):
            b = tuple(edges[i].replace(",","")+pesos[i])
            nuevo.append(b)
        return nuevo
    
    
    

# Ruta home 
@app.route('/')   
def home():
    return render_template('home.html')

# Ruta tarea 1 
@app.route('/tarea1', methods = ['GET', 'POST'])     #1. Pide los datos 
def tarea1():
    form = ClaseGrafo(request.form)
    if request.method == 'POST':
        if (form.dirigido.data)==True: #True el grafo es  dirigido
            Datos_Grafo = "D$"+str(form.nombre_grafico.data)+"$"+str(form.nombres_nodos.data)+"$"+str(form.edge.data)+"$"+str(form.pesos.data) #D confirma que es Dirigido, items = 5
        else:
            Datos_Grafo = str(form.nombre_grafico.data)+"$"+str(form.edge.data)+"$"+str(form.pesos.data) #No es dirigido, items =3
        return render_template("grafo.html", data = Datos_Grafo) #Envia la informacion como string a la funcion graph
    return render_template("tarea1.html", form = form)


@app.route('/graph/<string:data>')#2. URL recibe los datos.
def graph(data):
    corte_data = data.split("$") #division con tal de saber si es dirigido
    print(corte_data)

    if corte_data[0]=='D': #Si es dirigigo se usa el metodo DiGraph()
        G = nx.DiGraph()
        print(corte_data)
        edges_mas_pesos = procesado_formulario(corte_data) #Se envia a la funcion de recorte.
    else:
        G = nx.Graph() # en caso de no contener "D" se crea un metodo Graph()
        print(corte_data)
        edges_mas_pesos = procesado_formulario(corte_data) #Se envia a la funcion de recorte.
    print(edges_mas_pesos)
    G.add_weighted_edges_from(edges_mas_pesos) #4.Agrega los edges mas los pesos tipo [(1,2,peso)]
    nx.draw(G,with_labels=True) #with_labels=True muestra los numeros
    img = BytesIO() # file-like object for the image
    plt.savefig(img) # save the image to the stream
    img.seek(0) # writing moved the cursor to the end of the file, reset
    plt.clf() # clear pyplot
    return send_file(img, mimetype = 'image/png') #5.muestra la imagen por pantalla

#Se inicializa el servidor
if __name__=='__main__':
    app.run(debug=True)
