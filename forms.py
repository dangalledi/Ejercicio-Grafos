from wtforms import StringField, SubmitField, SelectField,Form
from wtforms.validators import DataRequired

#Creacion de clases donde se reciben los datos del formulario 
class ClaseGrafo(Form): 
    tipo = SelectField(u'tipo',choices = [('simple','Simple'),('direccionado','Direccionado')])
    vertices = StringField('Vertices',validators=[DataRequired()])
    aristas = StringField('Aristas',validators=[DataRequired()])
    submit = SubmitField('Ingresar')

class IngresoPeso(Form):
    arista= StringField('Arista',validators=[DataRequired()])
    peso= StringField('Peso',validators=[DataRequired()])
    submit = SubmitField('Ingresar')