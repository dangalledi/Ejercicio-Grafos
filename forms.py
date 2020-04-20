from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField,Form
from wtforms.validators import DataRequired

#Creacion de clases donde se reciben los datos del formulario 
class IngresoGrafo(Form): 
    etiquetado = BooleanField() # para saber si se etiqueta en la creación
    tipo = SelectField(u'tipo',choices = [('simple','Simple'),('direccionado','Direccionado')])
    vertices = StringField('Vertices',validators=[DataRequired()])
    aristas = StringField('Aristas',validators=[DataRequired()])
    submit = SubmitField('Ingresar')
