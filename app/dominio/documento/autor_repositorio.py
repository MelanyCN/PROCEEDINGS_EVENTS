from abc import ABC, abstractmethod

class AutorRepositorio(ABC):
    @abstractmethod
    def crear(self, autor):
        pass

    @abstractmethod
    def obtener(self, id):
        pass

    @abstractmethod
    def actualizar(self, autor):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass