from abc import ABC, abstractmethod
from .edicion import Edicion

class EdicionRepositorio(ABC):
    """Interfaz para el repositorio de Edicion. Define métodos CRUD esenciales."""

    @abstractmethod
    def crear(self, edicion: Edicion):
        """Crea una nueva edición en la base de datos.

        Args:
            edicion (Edicion): La edición a ser creada.
        """
        pass

    @abstractmethod
    def obtener(self, id: int) -> Edicion:
        """Obtiene una edición por su ID.

        Args:
            id (int): El ID de la edición a buscar.

        Returns:
            Edicion: La edición encontrada o None si no se encuentra.
        """
        pass

    @abstractmethod
    def actualizar(self, edicion: Edicion):
        """Actualiza una edición existente en la base de datos.

        Args:
            edicion (Edicion): La edición con los datos actualizados.
        """
        pass

    @abstractmethod
    def eliminar(self, id: int):
        """Elimina una edición de la base de datos por su ID.

        Args:
            id (int): El ID de la edición a eliminar.
        """
        pass
