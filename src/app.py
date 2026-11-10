from flask import Flask
from database import init_db
from controllers import producto_controller

# Inicializar la aplicación Flask
app = Flask(__name__)

# Inicializar la base de datos y las tablas al arrancar el servidor
init_db()

# Registrar el controlador con el prefijo '/api'
app.register_blueprint(producto_controller, url_prefix='/api')

# Ruta de bienvenida general
@app.route('/')
def home():
    return {
        "estado": "OK",
        "mensaje": "Bienvenido a la prueba de CRUD",
        "endpoints_disponibles": "/api/productos"
    }

if __name__ == '__main__':
    app.run(debug=True, port=5000)