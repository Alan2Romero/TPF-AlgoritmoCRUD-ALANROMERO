from flask import Blueprint, jsonify, request
from models import ProductoModel

producto_controller = Blueprint('producto_controller', __name__)

# GET: Listar todos los productos con su categoria relacionada
@producto_controller.route('/productos', methods=['GET'])
def obtener_productos():
    try:
        productos = ProductoModel.get_all()
        return jsonify(productos), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# POST: Crear un nuevo producto
@producto_controller.route('/productos', methods=['POST'])
def crear_producto():
    data = request.get_json()
    nombre = data.get('nombre')
    precio = data.get('precio')
    categoria_id = data.get('categoria_id')
    
    # Validacion de datos obligatorios
    if not nombre or not precio:
        return jsonify({"error": "El nombre y el precio son obligatorios"}), 400
        
    try:
        ProductoModel.create(nombre, precio, categoria_id)
        return jsonify({"mensaje": "Producto creado con exito"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# PUT: Actualizar un producto existente
@producto_controller.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    data = request.get_json()
    nombre = data.get('nombre')
    precio = data.get('precio')
    categoria_id = data.get('categoria_id')
    
    if not nombre or not precio:
        return jsonify({"error": "El nombre y el precio son obligatorios"}), 400
        
    try:
        ProductoModel.update(id, nombre, precio, categoria_id)
        return jsonify({"mensaje": f"Producto {id} actualizado con exito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# DELETE: Eliminar un producto
@producto_controller.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    try:
        ProductoModel.delete(id)
        return jsonify({"mensaje": f"Producto {id} eliminado con exito"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500