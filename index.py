from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tarea1', strict_slashes=False)
def tarea1():
    return render_template("tarea1.html")

if __name__=='__main__':
    app.run(debug=True)