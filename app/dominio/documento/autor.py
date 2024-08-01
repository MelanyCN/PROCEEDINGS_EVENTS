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
    
    @abstractmethod
    def listar_autores(self, id_documento):
        pass

class Autor:
    def __init__(self, id=None, nombre=None, email=None, afiliacion=None, nacionalidad=None, area_interes=None, link_foto=None):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.afiliacion = afiliacion
        self.nacionalidad = nacionalidad
        self.area_interes = area_interes
        self.link_foto = link_foto

    def __repr__(self):
        return f"Autor(id={self.id}), nombre='{self.nombre}', email='{self.email}', afiliacion='{self.afiliacion}', nacionalidad='{self.nacionalidad}', area_interes='{self.area_interes}', link_foto='{self.link_foto}')"

    def actualizar_email(self, nuevo_email):
        self.email = nuevo_email

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "afiliacion": self.afiliacion,
            "nacionalidad": self.nacionalidad,
            "area_interes": self.area_interes,
            "link_foto": self.link_foto
        }


