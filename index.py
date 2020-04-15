from flask import Flask, render_template, request, url_for, redirect
from forms import IngresoGrafo
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tarea1', methods=['GET', 'POST'])
def tarea1():
    form = IngresoGrafo()
    return render_template("tarea1.html",title="ingrese grafo", form=form)

if __name__=='__main__':
    app.run(debug=True)