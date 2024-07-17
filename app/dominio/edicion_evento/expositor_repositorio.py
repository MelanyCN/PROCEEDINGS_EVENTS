from abc import ABC, abstractmethod

class ExpositorRepositorio(ABC):
    @abstractmethod
    def crear(self, expositor):
        pass

    @abstractmethod
    def obtener(self, id):
        pass

    @abstractmethod
    def actualizar(self, expositor):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass