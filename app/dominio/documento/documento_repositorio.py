from abc import ABC, abstractmethod

class DocumentoRepositorio(ABC):
    @abstractmethod
    def crear(self, documento):
        pass

    @abstractmethod
    def obtener(self, id):
        pass

    @abstractmethod
    def actualizar(self, documento):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass