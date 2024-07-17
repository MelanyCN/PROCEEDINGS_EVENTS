from flask import Flask, request, jsonify
from mongoengine import connect
from app.infraestructura.repositorio.mongoDB import DocumentoRepositorioImpl
from app.infraestructura.repositorio.mongoDB.autor_repositorio_impl import AutorRepositorioImpl
from app.dominio.documento.documento import Documento  # Assuming 'Documento' is in 'app.dominio.modelo.documento'
from app.aplicacion.controller.documento_controller_impl import DocumentoControllerImpl
app = Flask(__name__)

# Configurar la base de datos
connect('base_de_datos')

# Configurar repositorios y controladores
documento_repo = DocumentoRepositorioImpl()
autor_repo = AutorRepositorioImpl()
documento_controller = DocumentoControllerImpl(documento_repo)

@app.route('/documento', methods=['POST'])
def crear_documento():
    data = request.get_json()
    documento = Documento(**data)
    documento_controller.crear_documento(documento)
    return jsonify(documento.to_json()), 201

@app.route('/documento/<id>', methods=['GET'])
def obtener_documento(id):
    documento = documento_controller.obtener_documento(id)
    if documento:
        return jsonify(documento.to_json())
    else:
        return jsonify({"error : Documento no encontrado"}), 404

@app.route('/documento/<id>', methods=['PUT'])
def actualizar_documento(id):
    data = request.get_json()
    documento = documento_controller.obtener_documento(id)
    if documento:
        documento.update(**data)
        documento_controller.actualizar_documento(documento)
        return jsonify(documento.to_json())
    else:
        return jsonify({"error": "Documento no encontrado"}), 404

@app.route('/documento/<id>', methods=['DELETE'])
def eliminar_documento(id):
    documento = documento_controller.eliminar_documento(id)
    if documento:
        return jsonify({"mensaje": "Documento eliminado"}), 200
    else:
        return jsonify({"error": "Documento no encontrado"}), 404

# Rutas para otros CRUDs

if __name__ == '__main__':
    app.run(debug=True)
