from abc import ABC, abstractmethod
from .inscripcion import Inscripcion

class InscripcionRepositorio(ABC):
    """Interfaz para el repositorio de Inscripcion. Define métodos CRUD esenciales."""

    @abstractmethod
    def crear(self, inscripcion: Inscripcion):
        """Crea una nueva inscripción en la base de datos.

        Args:
            inscripcion (Inscripcion): La inscripción a ser creada.
        """
        pass

    @abstractmethod
    def obtener(self, id: int) -> Inscripcion:
        """Obtiene una inscripción por su ID.

        Args:
            id (int): El ID de la inscripción a buscar.

        Returns:
            Inscripcion: La inscripción encontrada o None si no se encuentra.
        """
        pass

    @abstractmethod
    def actualizar(self, inscripcion: Inscripcion):
        """Actualiza una inscripción existente en la base de datos.

        Args:
            inscripcion (Inscripcion): La inscripción con los datos actualizados.
        """
        pass

    @abstractmethod
    def eliminar(self, id: int):
        """Elimina una inscripción de la base de datos por su ID.

        Args:
            id (int): El ID de la inscripción a eliminar.
        """
        pass
