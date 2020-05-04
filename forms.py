from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField,FloatField
from wtforms.validators import DataRequired

#Creacion de clases donde se reciben los datos del formulario 
class ClaseGrafo(FlaskForm): 
    nombre = StringField("Nombre",validators=[DataRequired()])
    etiquetado = BooleanField()
    tipo = SelectField('Tipo: ',choices = [('simple','Simple'),('direccionado','Direccionado')])
    nodos = StringField('Vertices\n(Ej: Talca, Paris, Londres) de <b>NO</b> ser etiquetado... <b>ingresar simplemente el n° de nodos</b>',validators=[DataRequired()])
    vertices = 0
    aristas = []
    vectores = []
    submit = SubmitField('      Crear       ')
    
class PostForm(FlaskForm):
    origen = SelectField("Origen: ", choices = [ ]) #
    destino = SelectField("Destino: ",choices = [ ]) #
    tarea = SelectField('Tarea: ', choices = [('actualizar','Actualizar grafo'),('agregar','Agregar arista al Grafo'),('corto','Mostrar camino más corto'),('flujo','Indicar el flujo máximo'),('hoe','Hamilton o Euler'),('arbol','Obtener Árbol Generador Mínimo'),('hamiltoniano','Grafo hamiltoniano'),('euleriano','Grafo euleriano'),('conexo','Saber si es conexo')])
    peso = FloatField("Peso: ",validators = [] ) 
    submit = SubmitField('      Realizar        ')