from abc import ABC, abstractmethod
from .evento import Evento

class EventoRepositorio(ABC):
    """Interfaz para el repositorio de Evento. Define métodos CRUD esenciales."""

    @abstractmethod
    def crear(self, evento: Evento):
        """Crea un nuevo evento en la base de datos.

        Args:
            evento (Evento): El evento a ser creado.
        """
        pass

    @abstractmethod
    def obtener(self, id: int) -> Evento:
        """Obtiene un evento por su ID.

        Args:
            id (int): El ID del evento a buscar.

        Returns:
            Evento: El evento encontrado o None si no se encuentra.
        """
        pass

    @abstractmethod
    def actualizar(self, evento: Evento):
        """Actualiza un evento existente en la base de datos.

        Args:
            evento (Evento): El evento con los datos actualizados.
        """
        pass

    @abstractmethod
    def eliminar(self, id: int) -> Evento:
        """Elimina un evento de la base de datos por su ID.

        Args:
            id (int): El ID del evento a eliminar.
        """
        pass
