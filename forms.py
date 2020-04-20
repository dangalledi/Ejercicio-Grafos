from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField, validators


#Creacion de clases donde se reciben los datos del formulario 
class IngresoGrafo(Form): 
    vertices= StringField('Vertices',[validators.DataRequired(),validators.length(min=1,max=3, message='Ingrese la cantidad de vertices')])
    aristas= StringField('Aristas',[validators.DataRequired(),validators.length(min=1,max=3, message='Ingrese la cantidad de aristas')])
    submit = SubmitField('Ingresar')
