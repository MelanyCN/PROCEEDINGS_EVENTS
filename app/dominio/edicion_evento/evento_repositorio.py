from abc import ABC, abstractmethod

class EventoRepositorio(ABC):
    @abstractmethod
    def crear(self, evento):
        pass

    @abstractmethod
    def obtener(self, id):
        pass

    @abstractmethod
    def actualizar(self, evento):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass