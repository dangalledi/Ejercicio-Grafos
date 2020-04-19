from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

#Creacion de clases donde se reciben los datos del formulario 
class IngresoGrafo(Form): 
    vertices= StringField('Vertices',validators=[DataRequired()])
    aristas= StringField('Aristas',validators=[DataRequired()])
    submit = SubmitField('Ingresar')
