from flask import request, jsonify

from app.infraestructura.repositorio.sqlite3.documento_repositorio_impl import DocumentoRepositorioImpl
from app.aplicacion.servicios.documento_servicio import DocumentoServicioImpl
from app.dominio.documento.documento import Documento

from app.infraestructura.repositorio.sqlite3.autor_repositorio_impl import AutorRepositorioImpl
from app.aplicacion.servicios.autor_servicio import AutorServicioImpl
from app.dominio.documento.autor import Autor

from app.dominio.excepciones import AutorRepositoryError, DocumentoRepositoryError



from datetime import datetime

documento_repo = DocumentoRepositorioImpl()
documento_servicio = DocumentoServicioImpl(documento_repo)

def configure_routes(app):
    """Configura las rutas de la aplicación."""
    configurar_rutas_documentos(app)

### Cookbook: Funciones Auxiliares
def documento_no_encontrado():
        """Devuelve una respuesta JSON indicando que el documento no fue encontrado."""
        return jsonify({"error": "Documento no encontrado"}), 404

def autor_no_encontrado():
        """Devuelve una respuesta JSON indicando que el documento no fue encontrado."""
        return jsonify({"error": "Autor no encontrado"}), 404

def parse_fecha(fecha_str):
    """Convierte una cadena de texto de fecha en un objeto datetime.date."""
    return datetime.strptime(fecha_str, "%Y-%m-%d").date() if fecha_str else None

def parse_autor(data):
    """Convierte un diccionario en un objeto Autor."""
    return Autor(**data) if data else None

def actualizar_atributos(obj, data):
    """Actualiza los atributos de un objeto con los datos proporcionados."""
    for key, value in data.items():
        setattr(obj, key, value)

### Configuración de rutas con Pipeline
def configurar_rutas_documentos(app):
    """Configura las rutas para documentos."""

    @app.route('/documento', methods=['POST'])
    def crear_documento():
        data = request.get_json()
        documento = Documento(
            titulo=data['titulo'],
            descripcion=data['descripcion'],
            fecha_publicacion=parse_fecha(data['fecha_publicacion']),
            autor=parse_autor(data['autor'])
        )
        documento_servicio.crear_documento(documento)
        return jsonify(documento.to_dict()), 201

    @app.route('/documento/<int:id>', methods=['GET'])
    def obtener_documento(id):
        documento = documento_servicio.obtener_documento(id)
        if documento:
            return jsonify(documento.to_dict())
        return jsonify({"error": documento_no_encontrado()}), 404

    @app.route('/documento/<int:id>', methods=['PUT'])
    def actualizar_documento(id):
        data = request.get_json()
        documento = documento_servicio.obtener_documento(id)
        if documento:
            actualizar_atributos(documento, data)
            documento_servicio.actualizar_documento(documento)
            return jsonify(documento.to_dict())
        return jsonify({"error": documento_no_encontrado()}), 404

    @app.route('/documento/<int:id>', methods=['DELETE'])
    def eliminar_documento(id):
        if documento_servicio.eliminar_documento(id):
            return jsonify({"mensaje": "Documento eliminado"}), 200
        return jsonify({"error": documento_no_encontrado()}), 404


    @app.route('/autores', methods=['GET'])    
    def obtener_autores():
        """
        Endpoint para obtener todos los autores.
        
        Returns:
            Response: Una respuesta JSON con la lista de autores.
        """
        try:
            autores = autor_servicio.obtener_todos_los_autores()
            return jsonify([autor.to_dict() for autor in autores])
        except AutorRepositoryError as e:
            return make_response(jsonify({"error": str(e)}), 500)
        except Exception as e:
            return make_response(jsonify({"error": f"Error inesperado: {e}"}), 500)
