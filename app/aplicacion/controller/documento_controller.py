from abc import ABC, abstractmethod

class DocumentoController(ABC):
    @abstractmethod
    def crear_documento(self, documento):
        pass

    @abstractmethod
    def obtener_documento(self, id):
        pass

    @abstractmethod
    def actualizar_documento(self, documento):
        pass

    @abstractmethod
    def eliminar_documento(self, id):
        pass