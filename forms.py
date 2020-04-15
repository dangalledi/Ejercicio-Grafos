from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class IngresoGrafo(FlaskForm):
    aristas= StringField('Aristas',validators=[DataRequired()])
    vertices= StringField('Vertices',validators=[DataRequired()])
    submit = SubmitField('Ingresar')
