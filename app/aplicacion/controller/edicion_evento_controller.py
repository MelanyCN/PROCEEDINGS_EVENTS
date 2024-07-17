from abc import ABC, abstractmethod

class EdicionEventoController(ABC):
    @abstractmethod
    def crear_edicion(self, edicion):
        pass

    @abstractmethod
    def obtener_edicion(self, id):
        pass

    @abstractmethod
    def actualizar_edicion(self, edicion):
        pass

    @abstractmethod
    def eliminar_edicion(self, id):
        pass