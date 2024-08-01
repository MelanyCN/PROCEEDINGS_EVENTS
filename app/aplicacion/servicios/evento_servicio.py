from abc import ABC, abstractmethod
from app.dominio.evento.evento import Evento
from app.dominio.evento.evento import EventoRepositorio

from app.dominio.evento.edicion import Edicion
from app.dominio.evento.edicion import EdicionRepositorio

# Interfaces para servicios
class EventoServicio(ABC):
    @abstractmethod
    def crear_evento(self, evento: Evento):
        pass

    @abstractmethod
    def obtener_evento(self, id: int) -> Evento:
        pass

    @abstractmethod
    def actualizar_evento(self, evento: Evento):
        pass

    @abstractmethod
    def eliminar_evento(self, id: int):
        pass

# Implementación del servicio de eventos
class EventoServicioImpl(EventoServicio):
    def __init__(self, evento_repo: EventoRepositorio, edicion_repo: EdicionRepositorio):
        """
        Inicializa el servicio con repositorios de eventos y ediciones.
        
        Args:
            evento_repo (EventoRepositorio): Repositorio para operaciones de evento.
            edicion_repo (EdicionRepositorio): Repositorio para operaciones de edición.
        """
        self.evento_repo = evento_repo
        self.edicion_repo = edicion_repo

    def crear_evento(self, evento: Evento):
        """
        Crea un nuevo evento en el repositorio.
        
        Args:
            evento (Evento): Evento a ser creado.
        """
        if evento.edicion_id:
            edicion = self.edicion_repo.obtener(evento.edicion_id)
            if not edicion:
                raise ValueError("Edición no encontrada.")
        self.evento_repo.crear(evento)

    def obtener_evento(self, id: int) -> Evento:
        """
        Obtiene un evento por su ID.
        
        Args:
            id (int): ID del evento.
            
        Returns:
            Evento: El evento encontrado.
        """
        evento = self.evento_repo.obtener(id)
        if evento and evento.edicion_id:
            evento.edicion = self.edicion_repo.obtener(evento.edicion_id)
        return evento

    def actualizar_evento(self, evento: Evento):
        """
        Actualiza un evento existente.
        
        Args:
            evento (Evento): Evento con datos actualizados.
        """
        if evento.edicion_id:
            edicion = self.edicion_repo.obtener(evento.edicion_id)
            if not edicion:
                raise ValueError("Edición no encontrada.")
        self.evento_repo.actualizar(evento)

    def eliminar_evento(self, id: int):
        """
        Elimina un evento por su ID.
        
        Args:
            id (int): ID del evento a eliminar.
        """
        self.evento_repo.eliminar(id)
