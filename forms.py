from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

#Creacion de clases donde se reciben los datos del formulario 
class ClaseGrafo(FlaskForm): 
    nombre = StringField("Nombre",validators=[DataRequired()])
    etiquetado = BooleanField()
    tipo = SelectField(u'tipo',choices = [('simple','Simple'),('direccionado','Direccionado')])
    nodos = StringField('Vertices\n(Ej: Talca, Paris, Londres) de <b>NO</b> ser etiquetado... <b>ingresar simplemente el n° de nodos</b>',validators=[DataRequired()])
    vertices = 0
    aristas = []
    vectores = []
    # IMPLEMENTAR ATRIBUTO MATRIZ
    submit = SubmitField('      Crear       ')
    
class PostForm(FlaskForm):
    origen = SelectField("Origen: ", choices = [ ]) #
    destino = SelectField("Destino: ",choices = [ ]) #
    tarea = SelectField('Tarea: ', choices = [('actualizar','Actualizar grafo'),('agregar','Agregar arista al Grafo'),('corto','Mostrar camino más corto'),('flujo','Indicar el flujo máximo'),('hoe','Hamilton o Euler'),('conexo','Saber si es conexo'),('kruskal','Obtener Árbol (KRUSKAL)')])
    peso = StringField("Peso: ",validators = [] ) # [DataRequired()]
    submit = SubmitField('      Realizar        ')