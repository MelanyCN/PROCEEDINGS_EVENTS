from abc import ABC, abstractmethod
from app.dominio.evento.edicion import Edicion

class EdicionController(ABC):
    @abstractmethod
    def crear_edicion(self, edicion: Edicion):
        pass

    @abstractmethod
    def obtener_edicion(self, id: int) -> Edicion:
        pass

    @abstractmethod
    def actualizar_edicion(self, edicion: Edicion):
        pass

    @abstractmethod
    def eliminar_edicion(self, id: int):
        pass
