from abc import ABC, abstractmethod
from .programa import Programa

class ProgramaRepositorio(ABC):
    """Interfaz para el repositorio de Programa. Define métodos CRUD esenciales."""

    @abstractmethod
    def crear(self, programa: Programa):
        """Crea un nuevo programa en la base de datos.

        Args:
            programa (Programa): El programa a ser creado.
        """
        pass

    @abstractmethod
    def obtener(self, id: int) -> Programa:
        """Obtiene un programa por su ID.

        Args:
            id (int): El ID del programa a buscar.

        Returns:
            Programa: El programa encontrado o None si no se encuentra.
        """
        pass

    @abstractmethod
    def actualizar(self, programa: Programa):
        """Actualiza un programa existente en la base de datos.

        Args:
            programa (Programa): El programa con los datos actualizados.
        """
        pass

    @abstractmethod
    def eliminar(self, id: int):
        """Elimina un programa de la base de datos por su ID.

        Args:
            id (int): El ID del programa a eliminar.
        """
        pass
