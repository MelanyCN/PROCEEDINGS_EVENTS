from abc import ABC, abstractmethod
from app.dominio.evento.expositor import Expositor, ExpositorRepositorio

# Interfaces para servicios
class ExpositorServicio(ABC):
    @abstractmethod
    def crear_expositor(self, expositor: Expositor):
        pass

    @abstractmethod
    def obtener_expositor(self, id: int) -> Expositor:
        pass

    @abstractmethod
    def actualizar_expositor(self, expositor: Expositor):
        pass

    @abstractmethod
    def eliminar_expositor(self, id: int):
        pass

# Implementación del servicio de expositores
class ExpositorServicioImpl(ExpositorServicio):
    def __init__(self, expositor_repo: ExpositorRepositorio):
        """
        Inicializa el servicio con un repositorio de expositores.
        
        Args:
            expositor_repo (ExpositorRepositorio): Repositorio para operaciones de expositor.
        """
        self.expositor_repo = expositor_repo

    def crear_expositor(self, expositor: Expositor):
        """
        Crea un nuevo expositor en el repositorio.
        
        Args:
            expositor (Expositor): Expositor a ser creado.
        """
        self.expositor_repo.crear(expositor)

    def obtener_expositor(self, id: int) -> Expositor:
        """
        Obtiene un expositor por su ID.
        
        Args:
            id (int): ID del expositor.
            
        Returns:
            Expositor: El expositor encontrado o None si no se encuentra.
        """
        return self.expositor_repo.obtener(id)

    def actualizar_expositor(self, expositor: Expositor):
        """
        Actualiza un expositor existente.
        
        Args:
            expositor (Expositor): Expositor con datos actualizados.
        """
        self.expositor_repo.actualizar(expositor)

    def eliminar_expositor(self, id: int):
        """
        Elimina un expositor por su ID.
        
        Args:
            id (int): ID del expositor a eliminar.
        """
        self.expositor_repo.eliminar(id)