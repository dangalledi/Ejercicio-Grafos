from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

#Creacion de clases donde se reciben los datos del formulario 
class ClaseGrafo(FlaskForm): 
    nombre = StringField("Nombre",validators=[DataRequired()])
    #etiquetado = BooleanField() # para saber si se etiqueta en la creación
    tipo = SelectField(u'tipo',choices = [('simple','Simple'),('direccionado','Direccionado')])
    nodos = StringField('Vertices\n(Ej: Talca, Paris, Londres) de ser no etiquetado ingresar el n° de nodos',validators=[DataRequired()])
    vertices = 0
    submit = SubmitField('Ingresar')
