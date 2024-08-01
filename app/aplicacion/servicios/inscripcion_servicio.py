from abc import ABC, abstractmethod
from app.dominio.evento.inscripcion import Inscripcion, InscripcionRepositorio

# Interfaces para servicios
class InscripcionServicio(ABC):
    @abstractmethod
    def crear_inscripcion(self, inscripcion: Inscripcion):
        pass

    @abstractmethod
    def obtener_inscripcion(self, id: int) -> Inscripcion:
        pass

    @abstractmethod
    def actualizar_inscripcion(self, inscripcion: Inscripcion):
        pass

    @abstractmethod
    def eliminar_inscripcion(self, id: int):
        pass

# Implementación del servicio de inscripciones
class InscripcionServicioImpl(InscripcionServicio):
    def __init__(self, inscripcion_repo: InscripcionRepositorio):
        """
        Inicializa el servicio con un repositorio de inscripciones.
        
        Args:
            inscripcion_repo (InscripcionRepositorio): Repositorio para operaciones de inscripción.
        """
        self.inscripcion_repo = inscripcion_repo

    def crear_inscripcion(self, inscripcion: Inscripcion):
        """
        Crea una nueva inscripción en el repositorio.
        
        Args:
            inscripcion (Inscripcion): Inscripción a ser creada.
        """
        self.inscripcion_repo.crear(inscripcion)

    def obtener_inscripcion(self, id: int) -> Inscripcion:
        """
        Obtiene una inscripción por su ID.
        
        Args:
            id (int): ID de la inscripción.
            
        Returns:
            Inscripcion: La inscripción encontrada o None si no se encuentra.
        """
        return self.inscripcion_repo.obtener(id)

    def actualizar_inscripcion(self, inscripcion: Inscripcion):
        """
        Actualiza una inscripción existente.
        
        Args:
            inscripcion (Inscripcion): Inscripción con datos actualizados.
        """
        self.inscripcion_repo.actualizar(inscripcion)

    def eliminar_inscripcion(self, id: int):
        """
        Elimina una inscripción por su ID.
        
        Args:
            id (int): ID de la inscripción a eliminar.
        """
        self.inscripcion_repo.eliminar(id)