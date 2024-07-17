from abc import ABC, abstractmethod

class ConvocatoriaRepositorio(ABC):
    @abstractmethod
    def crear(self, convocatoria):
        pass

    @abstractmethod
    def obtener(self, id):
        pass

    @abstractmethod
    def actualizar(self, convocatoria):
        pass

    @abstractmethod
    def eliminar(self, id):
        pass