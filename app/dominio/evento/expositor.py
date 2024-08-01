from abc import ABC, abstractmethod

class Expositor:
    def __init__(self, id, nombre, apellido, ocupacion, email, img_perfil_url, trayectoria_academica, evento_id):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.ocupacion = ocupacion
        self.email = email
        self.img_perfil_url = img_perfil_url
        self.trayectoria_academica = trayectoria_academica
        self.evento_id = evento_id

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "ocupacion": self.ocupacion,
            "email": self.email,
            "img_perfil_url": self.img_perfil_url,
            "trayectoria_academica": self.trayectoria_academica,
            "evento_id": self.evento_id
        }

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