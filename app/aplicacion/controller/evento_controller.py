from abc import ABC, abstractmethod
from app.dominio.evento.evento import Evento
from app.dominio.evento.edicion import Edicion
from app.dominio.evento.evento_repositorio import EventoRepositorio
from app.dominio.evento.edicion_repositorio import EdicionRepositorio

# Interfaces para controladores
class EventoController(ABC):
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

class EdicionController(ABC):
    @abstractmethod
    def crear_edicion(self, edicion: Edicion):
        pass

    @abstractmethod
    def obtener_edicion(self, id: int) -> Edicion:
        pass

    @abstractmethod
    def actualizar_edicion(self, edicion: Edicion):
        pass

    @abstractmethod
    def eliminar_edicion(self, id: int):
        pass

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

# Implementación del controlador de ediciones
class EdicionControllerImpl(EdicionController):
    def __init__(self, edicion_repo: EdicionRepositorio):
        """
        Inicializa el controlador con un repositorio de ediciones.
        
        Args:
            edicion_repo (EdicionRepositorio): Repositorio para operaciones de ediciones.
        """
        self.edicion_repo = edicion_repo

    def crear_edicion(self, edicion: Edicion):
        """
        Crea una nueva edición para un evento.
        
        Args:
            edicion (Edicion): Edición a ser creada.
        """
        self.edicion_repo.crear(edicion)

    def obtener_edicion(self, id: int) -> Edicion:
        """
        Obtiene una edición por su ID.
        
        Args:
            id (int): ID de la edición.
            
        Returns:
            Edicion: La edición encontrada.
        """
        return self.edicion_repo.obtener(id)

    def actualizar_edicion(self, edicion: Edicion):
        """
        Actualiza una edición existente.
        
        Args:
            edicion (Edicion): Edición con datos actualizados.
        """
        self.edicion_repo.actualizar(edicion)

    def eliminar_edicion(self, id: int):
        """
        Elimina una edición por su ID.
        
        Args:
            id (int): ID de la edición a eliminar.
        """
        self.edicion_repo.eliminar(id)
