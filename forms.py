from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField,Form
from wtforms.validators import DataRequired
import networkx as nx  

#Creacion de clases donde se reciben los datos del formulario 
class ClaseGrafo(Form): 
    nombre = StringField("Nombre",validators=[DataRequired()])
    tipo = SelectField(u'tipo',choices = [('simple','Simple'),('direccionado','Direccionado')])
    vertices = StringField('Vertices',validators=[DataRequired()])
    aristas = StringField('Aristas',validators=[DataRequired()])
    submit = SubmitField('Ingresar')
