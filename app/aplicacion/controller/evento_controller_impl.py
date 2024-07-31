from app.aplicacion.controller.evento_controller import EventoController
from app.dominio.evento.evento_repositorio import EventoRepositorio
from app.dominio.evento.evento import Evento

# Implementación del controlador de eventos
class EventoControllerImpl(EventoController):
    def __init__(self, evento_repo: EventoRepositorio):
        """
        Inicializa el controlador con un repositorio de eventos.
        
        Args:
            evento_repo (EventoRepositorio): Repositorio para operaciones de evento.
        """
        self.evento_repo = evento_repo

    def crear_evento(self, evento: Evento):
        """
        Crea un nuevo evento en el repositorio.
        
        Args:
            evento (Evento): Evento a ser creado.
        """
        self.evento_repo.crear(evento)

    def obtener_evento(self, id: int) -> Evento:
        """
        Obtiene un evento por su ID.
        
        Args:
            id (int): ID del evento.
            
        Returns:
            Evento: El evento encontrado.
        """
        return self.evento_repo.obtener(id)

    def actualizar_evento(self, evento: Evento):
        """
        Actualiza un evento existente.
        
        Args:
            evento (Evento): Evento con datos actualizados.
        """
        self.evento_repo.actualizar(evento)

    def eliminar_evento(self, id: int):
        """
        Elimina un evento por su ID.
        
        Args:
            id (int): ID del evento a eliminar.
        """
        self.evento_repo.eliminar(id)