from flask import Flask

app = Flask(__name__)

# Esta es la página de inicio y servicios
@app.route('/')
def inicio():
    return "Página de inicio y servicios"

@app.route('/productos')
def productos():
    return "Listado de productos"

@app.route('/equipo')
def equipo():
    return "Equipo humano"

@app.route('/contacto')
def contacto():
    return "Formulario de contacto"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)