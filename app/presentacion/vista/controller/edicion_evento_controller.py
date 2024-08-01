from app.infraestructura.repositorio.sqlite3.evento_repositorio_impl import EventoRepositorioImpl
from app.aplicacion.servicios.evento_servicio import EventoServicioImpl
from app.infraestructura.modelo.evento_modelo import EventoModelo 

from app.aplicacion.servicios.edicion_servicio import EdicionServicioImpl
from app.infraestructura.repositorio.sqlite3.edicion_repositorio_impl import EdicionRepositorioImpl
from app.dominio.evento.edicion import Edicion

from datetime import datetime

# Configuración de repositorios y controladores
evento_repo = EventoRepositorioImpl()
evento_servicio = EventoServicioImpl(evento_repo)

edicion_repo = EdicionRepositorioImpl()
edicion_servicio = EdicionServicioImpl(edicion_repo)

# Constantes para mensajes de error
EVENTO_NO_ENCONTRADO = "Evento no encontrado"
EDICION_NO_ENCONTRADA = "Edición no encontrada"

def configure_routes(app):
    """Configura las rutas de la aplicación."""
    configurar_rutas_eventos(app)
    configurar_rutas_ediciones(app)
