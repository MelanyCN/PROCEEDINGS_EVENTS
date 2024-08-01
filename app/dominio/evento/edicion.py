from abc import ABC, abstractmethod

class Edicion:
    def __init__(self, id, evento_id, nombre, fecha):
        self.id = id
        self.evento_id = evento_id
        self.nombre = nombre
        self.fecha = fecha

    def to_dict(self):
        return {
            "id": self.id,
            "evento_id": self.evento_id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }
    
    @staticmethod
    def from_dict(data):
        return Edicion(
            id=data.get('id'),
            evento_id=data.get('evento_id'),
            nombre=data.get('nombre'),
            fecha=data.get('fecha')
        )

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
