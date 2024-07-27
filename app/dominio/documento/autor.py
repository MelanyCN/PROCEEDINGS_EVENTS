from abc import ABC, abstractmethod

# Entidad
class Autor:
    def __init__(self, id=None, nombre=None, email=None):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __repr__(self):
        return f"Autor(id={self.id}), nombre='{self.nombre}', email='{self.email}')"

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }

# Repositorio Abstracto
class AutorRepositorio(ABC):
    @abstractmethod
    def crear(self, autor: Autor):
        pass

    @abstractmethod
    def obtener(self, id: str):
        pass

    @abstractmethod
    def actualizar(self, autor: Autor):
        pass

    @abstractmethod
    def eliminar(self, id: str):
        pass