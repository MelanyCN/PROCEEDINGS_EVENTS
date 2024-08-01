from abc import ABC, abstractmethod

class ConvocatoriaOrg:
    def __init__(self, id, nombre, fecha):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat()
        }

class ConvocatoriaOrgRepositorio(ABC):
    """Interfaz para el repositorio de ConvocatoriaOrg. Define métodos CRUD esenciales."""

    @abstractmethod
    def crear(self, convocatoria_org: ConvocatoriaOrg):
        """Crea una nueva convocatoria de organización en la base de datos.

        Args:
            convocatoria_org (ConvocatoriaOrg): La convocatoria de organización a ser creada.
        """
        pass

    @abstractmethod
    def obtener(self, id: int) -> ConvocatoriaOrg:
        """Obtiene una convocatoria de organización por su ID.

        Args:
            id (int): El ID de la convocatoria de organización a buscar.

        Returns:
            ConvocatoriaOrg: La convocatoria de organización encontrada o None si no se encuentra.
        """
        pass

    @abstractmethod
    def actualizar(self, convocatoria_org: ConvocatoriaOrg):
        """Actualiza una convocatoria de organización existente en la base de datos.

        Args:
            convocatoria_org (ConvocatoriaOrg): La convocatoria de organización con los datos actualizados.
        """
        pass

    @abstractmethod
    def eliminar(self, id: int):
        """Elimina una convocatoria de organización de la base de datos por su ID.

        Args:
            id (int): El ID de la convocatoria de organización a eliminar.
        """
        pass
