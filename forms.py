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
    tarea = SelectField("Tarea: ", choices = [("agregar","Agregar nodo al Grafo"),("corto","Mostrar camino más corto"),("flujo","Indicar el flujo máximo")])
    peso = StringField("Peso: ",validators = [] ) # [DataRequired()]
    submit = SubmitField('      Realizar        ')


def fix(vec,DIC):
        for i in range(len(DIC)):
            str1 = str(i)
            str2 = DIC[i]
            print(str1,str2)
            vec = vec.replace(str1,str2)
        v = vec.replace(' ','')#[(1,2,4),(2,3,5)]
        v = v.replace('[(','')#1,2,4),(2,3,5)]
        v= v.replace(')]','')#1,2,4),(2,3,5
        v= v.replace('),(',':')#1,2,4:2,3,5
        v = v.split(":")#['1,2,4', '2,3,5']

        n = []
        t = []
        for i in v: #['1,2,4', '2,3,5']
            c = i.split(",")#['1','2','4']
            for x in c:#'1'
                n.append(x)#str -> int
            t.append(tuple(n)) #t = [1,2,4.0]
            n = []
        return t