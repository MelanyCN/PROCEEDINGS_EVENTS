from flask import request, jsonify
from app.aplicacion.controller.documento_controller_impl import DocumentoControllerImpl
from app.infraestructura.repositorio.sqlite3.documento_repositorio_impl import DocumentoRepositorioImpl
from app.dominio.documento.documento import Documento
from app.dominio.documento.autor import Autor

from app.infraestructura.repositorio.sqlite3.evento_repositorio_impl import EventoRepositorioImpl
from app.aplicacion.controller.evento_controller_impl import EventoControllerImpl
from app.infraestructura.modelo.evento_modelo import EventoModelo  # Asegúrate de importar EventoModelo

from app.aplicacion.controller.edicion_controller_impl import EdicionControllerImpl
from app.infraestructura.repositorio.sqlite3.edicion_repositorio_impl import EdicionRepositorioImpl
from app.dominio.evento.edicion import Edicion

from datetime import datetime

# Configuración de repositorios y controladores
documento_repo = DocumentoRepositorioImpl()
documento_controller = DocumentoControllerImpl(documento_repo)

evento_repo = EventoRepositorioImpl()
evento_controller = EventoControllerImpl(evento_repo)

edicion_repo = EdicionRepositorioImpl()
edicion_controller = EdicionControllerImpl(edicion_repo)

# Constantes para mensajes de error
DOCUMENTO_NO_ENCONTRADO = "Documento no encontrado"
EVENTO_NO_ENCONTRADO = "Evento no encontrado"
EDICION_NO_ENCONTRADA = "Edición no encontrada"

def configure_routes(app):
    """Configura las rutas de la aplicación."""
    configurar_rutas_documentos(app)
    configurar_rutas_eventos(app)
    configurar_rutas_ediciones(app)

### Cookbook: Funciones Auxiliares
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
        documento_controller.crear_documento(documento)
        return jsonify(documento.to_dict()), 201

    @app.route('/documento/<int:id>', methods=['GET'])
    def obtener_documento(id):
        documento = documento_controller.obtener_documento(id)
        if documento:
            return jsonify(documento.to_dict())
        return jsonify({"error": DOCUMENTO_NO_ENCONTRADO}), 404

    @app.route('/documento/<int:id>', methods=['PUT'])
    def actualizar_documento(id):
        data = request.get_json()
        documento = documento_controller.obtener_documento(id)
        if documento:
            actualizar_atributos(documento, data)
            documento_controller.actualizar_documento(documento)
            return jsonify(documento.to_dict())
        return jsonify({"error": DOCUMENTO_NO_ENCONTRADO}), 404

    @app.route('/documento/<int:id>', methods=['DELETE'])
    def eliminar_documento(id):
        if documento_controller.eliminar_documento(id):
            return jsonify({"mensaje": "Documento eliminado"}), 200
        return jsonify({"error": DOCUMENTO_NO_ENCONTRADO}), 404

def configurar_rutas_eventos(app):
    """Configura las rutas para eventos."""
    @app.route('/evento', methods=['POST'])
    def crear_evento():
        try:
            data = request.get_json()
            nombre = data.get('nombre')
            fecha_str = data.get('fecha')
            fecha = parse_fecha(fecha_str)
            descripcion = data.get('descripcion')
            hora = data.get('hora')
            lugar = data.get('lugar')

            # Cookbook: Uso de función auxiliar para crear el evento
            evento_modelo = EventoModelo(nombre=nombre, fecha=fecha, descripcion=descripcion, hora=hora, lugar=lugar)
            evento_controller.crear_evento(evento_modelo)
            return jsonify(evento_modelo.to_dict()), 201
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/evento/<int:id>', methods=['GET'])
    def obtener_evento(id):
        evento = evento_controller.obtener_evento(id)
        if evento:
            return jsonify(evento.to_dict())
        else:
            return jsonify({"error": EVENTO_NO_ENCONTRADO}), 404

    @app.route('/evento/<int:id>', methods=['PUT'])
    def actualizar_evento(id):
        data = request.get_json()
        nombre = data.get('nombre')
        fecha_str = data.get('fecha')
        fecha = parse_fecha(fecha_str)

        # Error/Exception Handling
        try:
            evento = EventoModelo.query.get(id)
            if not evento:
                return jsonify({"error": EVENTO_NO_ENCONTRADO}), 404
            evento.nombre = nombre
            evento.fecha = fecha
            evento_controller.actualizar_evento(evento)
            return jsonify(evento.to_dict())
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/evento/<int:id>', methods=['DELETE'])
    def eliminar_evento(id):
        """Elimina un evento por su ID."""
        if not evento_controller.eliminar_evento(id):
            return jsonify({"mensaje": "Evento eliminado"}), 200
        return jsonify({"error": EVENTO_NO_ENCONTRADO}), 404

def configurar_rutas_ediciones(app):
    """Configura las rutas para ediciones."""
    @app.route('/evento/<int:evento_id>/edicion', methods=['POST'])
    def crear_edicion(evento_id):
        data = request.get_json()
        data['evento_id'] = evento_id
        edicion = Edicion(**data)
        edicion_controller.crear_edicion(edicion)
        return jsonify(edicion.to_dict()), 201

    @app.route('/evento/<int:evento_id>/edicion/<int:id>', methods=['GET'])
    def obtener_edicion(evento_id, id):
        edicion = edicion_controller.obtener_edicion(id)
        if edicion and edicion.evento_id == evento_id:
            return jsonify(edicion.to_dict())
        return jsonify({"error": EDICION_NO_ENCONTRADA}), 404

    @app.route('/evento/<int:evento_id>/edicion/<int:id>', methods=['PUT'])
    def actualizar_edicion(evento_id, id):
        data = request.get_json()
        edicion = edicion_controller.obtener_edicion(id)
        if edicion and edicion.evento_id == evento_id:
            actualizar_atributos(edicion, data)
            edicion_controller.actualizar_edicion(edicion)
            return jsonify(edicion.to_dict())
        return jsonify({"error": EDICION_NO_ENCONTRADA}), 404

    @app.route('/evento/<int:evento_id>/edicion/<int:id>', methods=['DELETE'])
    def eliminar_edicion(evento_id, id):
        edicion = edicion_controller.obtener_edicion(id)
        if edicion and edicion.evento_id == evento_id:
            edicion_controller.eliminar_edicion(id)
            return jsonify({"mensaje": "Edición eliminada"}), 200
        return jsonify({"error": EDICION_NO_ENCONTRADA}), 404
