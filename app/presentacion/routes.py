from flask import request, jsonify
from app.aplicacion.servicios.documento_servicio import DocumentoServicioImpl
from app.infraestructura.repositorio.sqlite3.documento_repositorio_impl import DocumentoRepositorioImpl
from app.dominio.documento.documento import Documento
from app.dominio.documento.autor import Autor

from app.infraestructura.repositorio.sqlite3.evento_repositorio_impl import EventoRepositorioImpl
from app.aplicacion.servicios.evento_servicio import EventoServicioImpl
from app.infraestructura.modelo.evento_modelo import EventoModelo

from app.aplicacion.servicios.edicion_servicio import EdicionServicioImpl
from app.infraestructura.repositorio.sqlite3.edicion_repositorio_impl import EdicionRepositorioImpl
from app.dominio.evento.edicion import Edicion

from app.dominio.evento.expositor import Expositor
from app.aplicacion.servicios.expositor_servicio import ExpositorServicioImpl
from app.infraestructura.repositorio.sqlite3.expositor_repositorio_impl import ExpositorRepositorioImpl

from app.aplicacion.servicios.convocatoria_org_servicio import ConvocatoriaOrgServicioImpl
from app.infraestructura.repositorio.sqlite3.convocatoria_org_repositorio_impl import ConvocatoriaOrgRepositorioImpl
from app.dominio.evento.convocatoria_org import ConvocatoriaOrg

from app.aplicacion.servicios.inscripcion_servicio import InscripcionServicioImpl
from app.infraestructura.repositorio.sqlite3.inscripcion_repositorio_impl import InscripcionRepositorioImpl
from app.dominio.evento.inscripcion import Inscripcion

from datetime import datetime

# Configuración de repositorios y controladores
documento_repo = DocumentoRepositorioImpl()
documento_servicio = DocumentoServicioImpl(documento_repo)

edicion_repo = EdicionRepositorioImpl()
edicion_servicio = EdicionServicioImpl(edicion_repo)

evento_repo = EventoRepositorioImpl()
evento_servicio = EventoServicioImpl(evento_repo, edicion_repo)

expositor_expo = ExpositorRepositorioImpl()
expositor_servicio = ExpositorServicioImpl(expositor_expo)

convocatoria_org_repo = ConvocatoriaOrgRepositorioImpl()
convocatoria_org_servicio = ConvocatoriaOrgServicioImpl(convocatoria_org_repo)

inscripcion_repo = InscripcionRepositorioImpl()
inscripcion_servicio = InscripcionServicioImpl(inscripcion_repo)

# Constantes para mensajes de error
DOCUMENTO_NO_ENCONTRADO = "Documento no encontrado"
EVENTO_NO_ENCONTRADO = "Evento no encontrado"
EDICION_NO_ENCONTRADA = "Edición no encontrada"
EXPOSITOR_NO_ENCONTRADO = "Expositor no encontrado"
CONVOCATORIA_NO_ENCONTRADA = "Convocatoria de organización no encontrada"
INSCRIPCION_NO_ENCONTRADA = "Inscripción no encontrada"

def configure_routes(app):
    """Configura las rutas de la aplicación."""
    configurar_rutas_documentos(app)
    configurar_rutas_eventos(app)
    configurar_rutas_ediciones(app)
    configurar_rutas_expositor(app)
    configurar_rutas_convocatorias(app)
    configurar_rutas_inscripciones(app)

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
        documento_servicio.crear_documento(documento)
        return jsonify(documento.to_dict()), 201

    @app.route('/documento/<int:id>', methods=['GET'])
    def obtener_documento(id):
        documento = documento_servicio.obtener_documento(id)
        if documento:
            return jsonify(documento.to_dict())
        return jsonify({"error": DOCUMENTO_NO_ENCONTRADO}), 404

    @app.route('/documento/<int:id>', methods=['PUT'])
    def actualizar_documento(id):
        data = request.get_json()
        documento = documento_servicio.obtener_documento(id)
        if documento:
            actualizar_atributos(documento, data)
            documento_servicio.actualizar_documento(documento)
            return jsonify(documento.to_dict())
        return jsonify({"error": DOCUMENTO_NO_ENCONTRADO}), 404

    @app.route('/documento/<int:id>', methods=['DELETE'])
    def eliminar_documento(id):
        if documento_servicio.eliminar_documento(id):
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
            evento_servicio.crear_evento(evento_modelo)
            return jsonify(evento_modelo.to_dict()), 201
        except Exception as e:
            return jsonify({"error":f"Error al crear evento: {str(e)}"}), 400

    @app.route('/evento/<int:id>', methods=['GET'])
    def obtener_evento(id):
        evento = evento_servicio.obtener_evento(id)
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
        descripcion = data.get('descripcion')
        hora = data.get('hora')
        lugar = data.get('lugar')

        # Error/Exception Handling
        try:
            evento = EventoModelo.query.get(id)
            if not evento:
                return jsonify({"error": EVENTO_NO_ENCONTRADO}), 404
            evento.nombre = nombre
            evento.fecha = fecha
            evento.descripcion = descripcion
            evento.hora = hora
            evento.lugar = lugar
            evento_servicio.actualizar_evento(evento)
            return jsonify(evento.to_dict())
        except Exception as e:
            return jsonify({"error": str(e)}), 400

    @app.route('/evento/<int:id>', methods=['DELETE'])
    def eliminar_evento(id):
        """Elimina un evento por su ID."""
        if not evento_servicio.eliminar_evento(id):
            return jsonify({"mensaje": "Evento eliminado"}), 200
        return jsonify({"error": EVENTO_NO_ENCONTRADO}), 404

def configurar_rutas_ediciones(app):
    """Configura las rutas para ediciones."""
    @app.route('/evento/<int:evento_id>/edicion', methods=['POST'])
    def crear_edicion(evento_id):
        try:
            data = request.get_json()
            data['evento_id'] = evento_id
            edicion = Edicion(
                id=None,
                evento_id=evento_id,
                nombre=data.get('nombre'),
                fecha=parse_fecha(data.get('fecha'))
            )
            edicion_servicio.crear_edicion(edicion)
            return jsonify(edicion.to_dict()), 201
        except Exception as e:
            return jsonify({"error": f"Error al crear la edición: {str(e)}"}), 500

    @app.route('/evento/<int:evento_id>/edicion/<int:id>', methods=['GET'])
    def obtener_edicion(evento_id, id):
        edicion = edicion_servicio.obtener_edicion(id)
        if edicion and edicion.evento_id == evento_id:
            return jsonify(edicion.to_dict())
        return jsonify({"error": EDICION_NO_ENCONTRADA}), 404

    @app.route('/evento/<int:evento_id>/edicion/<int:id>', methods=['PUT'])
    def actualizar_edicion(evento_id, id):
        data = request.get_json()
        edicion = edicion_servicio.obtener_edicion(id)
        if edicion and edicion.evento_id == evento_id:
            edicion.nombre = data.get('nombre', edicion.nombre)
            edicion.fecha = parse_fecha(data.get('fecha')) if data.get('fecha') else edicion.fecha
            edicion_servicio.actualizar_edicion(edicion)
            return jsonify(edicion.to_dict())
        return jsonify({"error": EDICION_NO_ENCONTRADA}), 404

    @app.route('/evento/<int:evento_id>/edicion/<int:id>', methods=['DELETE'])
    def eliminar_edicion(evento_id, id):
        edicion = edicion_servicio.obtener_edicion(id)
        if edicion and edicion.evento_id == evento_id:
            edicion_servicio.eliminar_edicion(id)
            return jsonify({"mensaje": "Edición eliminada"}), 200
        return jsonify({"error": EDICION_NO_ENCONTRADA}), 404
    
def configurar_rutas_expositor(app):
    """Configura las rutas para expositores."""

    @app.route('/expositor', methods=['POST'])
    def crear_expositor():
        data = request.get_json()
        expositor = Expositor(
            id=None,
            nombre=data.get('nombre'),
            apellido=data.get('apellido'),
            ocupacion=data.get('ocupacion'),
            email=data.get('email'),
            img_perfil_url=data.get('img_perfil_url'),
            trayectoria_academica=data.get('trayectoria_academica'),
            evento_id=data.get('evento_id')
        )
        try:
            expositor_servicio.crear_expositor(expositor)
            return jsonify(expositor.to_dict()), 201
        except Exception as e:
            return jsonify({"error": f"Error al crear expositor: {str(e)}"}), 400

    @app.route('/expositor/<int:id>', methods=['GET'])
    def obtener_expositor(id):
        expositor = expositor_servicio.obtener_expositor(id)
        if expositor:
            return jsonify(expositor.to_dict())
        return jsonify({"error": EXPOSITOR_NO_ENCONTRADO}), 404

    @app.route('/expositor/<int:id>', methods=['PUT'])
    def actualizar_expositor(id):
        data = request.get_json()
        expositor = expositor_servicio.obtener_expositor(id)
        if expositor:
            expositor.nombre = data.get('nombre', expositor.nombre)
            expositor.apellido = data.get('apellido', expositor.apellido)
            expositor.ocupacion = data.get('ocupacion', expositor.ocupacion)
            expositor.email = data.get('email', expositor.email)
            expositor.img_perfil_url = data.get('img_perfil_url', expositor.img_perfil_url)
            expositor.trayectoria_academica = data.get('trayectoria_academica', expositor.trayectoria_academica)
            expositor_servicio.actualizar_expositor(expositor)
            return jsonify(expositor.to_dict())
        return jsonify({"error": EXPOSITOR_NO_ENCONTRADO}), 404

    @app.route('/expositor/<int:id>', methods=['DELETE'])
    def eliminar_expositor(id):
        if not expositor_servicio.eliminar_expositor(id):
            return jsonify({"mensaje": "Expositor eliminado"}), 200
        return jsonify({"error": "Expositor no encontrado"}), 404
    
def configurar_rutas_convocatorias(app):
    """Configura las rutas para convocatorias de organización."""
    @app.route('/convocatoria_org', methods=['POST'])
    def crear_convocatoria_org():
        try:
            data = request.get_json()
            convocatoria_org = ConvocatoriaOrg(
                id=None,
                nombre=data.get('nombre'),
                fecha=datetime.strptime(data.get('fecha'), "%Y-%m-%d"),
                edicion_id=data.get('edicion_id')
            )
            convocatoria_org_servicio.crear_convocatoria_org(convocatoria_org)
            return jsonify(convocatoria_org.to_dict()), 201
        except Exception as e:
            return jsonify({"error": f"Error al crear convocatoria: {str(e)}"}), 400

    @app.route('/convocatoria_org/<int:id>', methods=['GET'])
    def obtener_convocatoria_org(id):
        try:
            convocatoria_org = convocatoria_org_servicio.obtener_convocatoria_org(id)
            if convocatoria_org:
                return jsonify(convocatoria_org.to_dict())
            else:
                return jsonify({"error": CONVOCATORIA_NO_ENCONTRADA}), 404
        except Exception as e:
            return jsonify({"error": f"Error al obtener convocatoria: {str(e)}"}), 400

    @app.route('/convocatoria_org/<int:id>', methods=['PUT'])
    def actualizar_convocatoria_org(id):
        try:
            data = request.get_json()
            convocatoria_org = convocatoria_org_servicio.obtener_convocatoria_org(id)
            if convocatoria_org:
                convocatoria_org.nombre = data.get('nombre', convocatoria_org.nombre)
                convocatoria_org.fecha = datetime.strptime(data.get('fecha'), "%Y-%m-%d")
                convocatoria_org.edicion_id = data.get('edicion_id', convocatoria_org.edicion_id)
                convocatoria_org_servicio.actualizar_convocatoria_org(convocatoria_org)
                return jsonify(convocatoria_org.to_dict())
            else:
                return jsonify({"error": CONVOCATORIA_NO_ENCONTRADA}), 404
        except Exception as e:
            return jsonify({"error": f"Error al actualizar convocatoria: {str(e)}"}), 400

    @app.route('/convocatoria_org/<int:id>', methods=['DELETE'])
    def eliminar_convocatoria_org(id):
        if not convocatoria_org_servicio.eliminar_convocatoria_org(id):
            return jsonify({"mensaje": "Convocatoria de organización eliminada"}), 200
        return jsonify({"error": CONVOCATORIA_NO_ENCONTRADA}), 404
    
def configurar_rutas_inscripciones(app):
    @app.route('/inscripcion', methods=['POST'])
    def crear_inscripcion():
        try:
            data = request.get_json()
            inscripcion = Inscripcion(
                id=None,
                nombre=data['nombre'],
                apellidos=data['apellidos'],
                dni=data['dni'],
                ocupacion=data['ocupacion'],
                correo=data['correo'],
                vaucher_url=data['vaucher_url'],
                evento_id=data['evento_id']
            )
            inscripcion_servicio.crear_inscripcion(inscripcion)
            return jsonify(inscripcion.to_dict()), 201
        except Exception as e:
            return jsonify({"error": f"Error al crear inscripción: {str(e)}"}), 400

    @app.route('/inscripcion/<int:id>', methods=['GET'])
    def obtener_inscripcion(id):
        inscripcion = inscripcion_servicio.obtener_inscripcion(id)
        if inscripcion:
            return jsonify(inscripcion.to_dict())
        return jsonify({"error": INSCRIPCION_NO_ENCONTRADA}), 404

    @app.route('/inscripcion/<int:id>', methods=['PUT'])
    def actualizar_inscripcion(id):
        try:
            data = request.get_json()
            inscripcion = inscripcion_servicio.obtener_inscripcion(id)
            if inscripcion:
                inscripcion.nombre = data.get('nombre', inscripcion.nombre)
                inscripcion.apellidos = data.get('apellidos', inscripcion.apellidos)
                inscripcion.dni = data.get('dni', inscripcion.dni)
                inscripcion.ocupacion = data.get('ocupacion', inscripcion.ocupacion)
                inscripcion.correo = data.get('correo', inscripcion.correo)
                inscripcion.vaucher_url = data.get('vaucher_url', inscripcion.vaucher_url)
                inscripcion.evento_id = data.get('evento_id', inscripcion.evento_id)
                inscripcion_servicio.actualizar_inscripcion(inscripcion)
                return jsonify(inscripcion.to_dict())
            return jsonify({"error": INSCRIPCION_NO_ENCONTRADA}), 404
        except Exception as e:
            return jsonify({"error": f"Error al actualizar inscripción: {str(e)}"}), 400

    @app.route('/inscripcion/<int:id>', methods=['DELETE'])
    def eliminar_inscripcion(id):
        try:
            if inscripcion_servicio.eliminar_inscripcion(id):
                return jsonify({"mensaje": "Inscripción eliminada"}), 200
            return jsonify({"error": INSCRIPCION_NO_ENCONTRADA}), 404
        except Exception as e:
            return jsonify({"error": f"Error al eliminar inscripción: {str(e)}"}), 400