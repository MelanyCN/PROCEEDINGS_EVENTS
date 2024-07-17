from abc import ABC, abstractmethod

class InscripcionRepositorio(ABC):
    @abstractmethod
    def crear(self, inscripcion):
        pass

    @abstractmethod
    def obtener(self, id):
        pass

    @abstractmethod
    def actualizar(self, inscripcion):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass