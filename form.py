from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

#Creacion de clases donde se reciben los datos del formulario 
class ClaseGrafo(FlaskForm): 
    nombre_grafico = StringField("Nombres grafico",validators=[DataRequired(),Length(min=1,max=1000)]) # para saber si se etiqueta en la creación
    dirigido = BooleanField() #Elimine Dirigido-simple ya que se infiere de la opcion.
    nombres_nodos = StringField("Nombres de los nodos, si no se agregan nombres mostrara los nodos comos numeros")
    edge = StringField('Agregar como = "1,2;2,3;3,2"  separando los edges con ";" y los nodos que componen la arista con ","',validators=[DataRequired(),Length(min=1,max=1000)])
    pesos = StringField('peso01,peso02 correspondiente al peso de los edges 1 y 2 y 2 y 3',validators=[DataRequired(),Length(min=1,max=1000)])
    submit = SubmitField('Ingresar')