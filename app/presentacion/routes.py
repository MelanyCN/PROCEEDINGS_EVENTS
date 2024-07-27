from flask import request, jsonify
from app.aplicacion.controller.documento_controller_impl import DocumentoControllerImpl
from app.infraestructura.repositorio.sqlite3.documento_repositorio_impl import DocumentoRepositorioImpl
from app.dominio.documento.documento import Documento
from app.dominio.documento.autor import Autor
from datetime import datetime

documento_repo = DocumentoRepositorioImpl()
documento_controller = DocumentoControllerImpl(documento_repo)

def configure_routes(app):

    def documento_no_encontrado():
        return jsonify({"error": "Documento no encontrado"}), 404

    @app.route('/documento', methods=['POST'])
    def crear_documento():
        data = request.get_json()
        
        fecha_publicacion = data.get('fecha_publicacion')
        if fecha_publicacion:
            data['fecha_publicacion'] = datetime.strptime(fecha_publicacion, "%Y-%m-%d").date()
        
        autor_data = data.pop('autor', {})
        autor = Autor(**autor_data)
        documento = Documento(autor=autor, **data)
        documento_controller.crear_documento(documento)
        return jsonify(documento.to_dict()), 201

    @app.route('/documento/<int:id>', methods=['GET'])
    def obtener_documento(id):
        documento = documento_controller.obtener_documento(id)
        if documento:
            return jsonify(documento.to_dict())
        else:
            return documento_no_encontrado()

    @app.route('/documento/<int:id>', methods=['PUT'])
    def actualizar_documento(id):
        data = request.get_json()
        documento = documento_controller.obtener_documento(id)
        if documento:
            for key, value in data.items():
                setattr(documento, key, value)
            documento_controller.actualizar_documento(documento)
            return jsonify(documento.to_dict())
        else:
            return documento_no_encontrado()

    @app.route('/documento/<int:id>', methods=['DELETE'])
    def eliminar_documento(id):
        resultado = documento_controller.eliminar_documento(id)
        if resultado:
            return jsonify({"mensaje": "Documento eliminado"}), 200
        else:
            return documento_no_encontrado()