from flask import Flask

app = Flask(__name__)

@app.route('/')
def inicio():
    return "hola mundo"

@app.route('/saludo')
def saludo():
    return "hola, como estas?"

@app.route('/saludo/<nombre>')
def saludo_nombre(nombre):
    return f"hola, {nombre}"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)