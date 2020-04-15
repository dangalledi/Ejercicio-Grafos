import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess' 
    # Esto lo puse en modo desesperacion porque no me funcionaba el formulario 
    # no se si en vdd funciona 
    # pero si es asi valdria una fortuna .. asjkasjkas naa mentira 
    
    #  Flask y algunas de sus extensiones utilizan el valor de la clave secreta como clave criptográfica, útil para generar firmas o tokens. La extensión Flask-WTF lo utiliza para proteger los formularios web contra un ataque desagradable llamado Cross-Site Request Forgery o CSRF
    # Osea creo que no se esta usando 