from abc import ABC, abstractmethod
from .expositor import Expositor

class ExpositorRepositorio(ABC):
    """Interfaz para el repositorio de Expositor. Define métodos CRUD esenciales."""

    @abstractmethod
    def crear(self, expositor: Expositor):
        """Crea un nuevo expositor en la base de datos.

        Args:
            expositor (Expositor): El expositor a ser creado.
        """
        pass

    @abstractmethod
    def obtener(self, id: int) -> Expositor:
        """Obtiene un expositor por su ID.

        Args:
            id (int): El ID del expositor a buscar.

        Returns:
            Expositor: El expositor encontrado o None si no se encuentra.
        """
        pass

    @abstractmethod
    def actualizar(self, expositor: Expositor):
        """Actualiza un expositor existente en la base de datos.

        Args:
            expositor (Expositor): El expositor con los datos actualizados.
        """
        pass

    @abstractmethod
    def eliminar(self, id: int):
        """Elimina un expositor de la base de datos por su ID.

        Args:
            id (int): El ID del expositor a eliminar.
        """
        pass
