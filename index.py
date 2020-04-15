from flask import Flask, render_template, request, url_for, redirect
from forms import IngresoGrafo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Ruta home 
@app.route('/')   
def home():
    return render_template('home.html')

# Ruta tarea 1 
@app.route('/tarea1', methods=['GET', 'POST'])      
def tarea1():
    form = IngresoGrafo()      # se guardan los datos obtenidos del formulario  

    return render_template("tarea1.html",title="ingrese grafo", form=form)

#Se inicializa el servidor
if __name__=='__main__':
    app.run(debug=True)