from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

#Creacion de clases donde se reciben los datos del formulario 
class IngresoGrafo(Form): 
    #ipo = SelectField(u'tipo',choices = [('Completo','completo'),('Direccionado','direccionado')])
    vertices = StringField('Vertices',validators=[DataRequired()])
    aristas = StringField('Aristas',validators=[DataRequired()])
    submit = SubmitField('Ingresar')
