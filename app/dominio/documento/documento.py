from .autor import Autor

from abc import ABC, abstractmethod
from typing import Optional
from datetime import datetime

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

    @abstractmethod
    def listar(self):
        pass

    
class Documento:
    def __init__(self, id=None, titulo=None, descripcion=None, fecha_publicacion=None,
                    link_imagen=None, link_documento=None, autor_id=None, autor=None):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_publicacion = fecha_publicacion
        self.link_imagen = link_imagen
        self.link_documento = link_documento
        self.autor_id = autor_id

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_publicacion": self.fecha_publicacion.isoformat() if self.fecha_publicacion else None,
            "link_imagen": self.link_imagen,
            "link_documento": self.link_documento,
            "autor_id": self.autor_id
        }

    @staticmethod
    def from_dict(data):
        return Documento(
            id=data.get('id'),
            titulo=data.get('titulo'),
            descripcion=data.get('descripcion'),
            fecha_publicacion=data.get('fecha_publicacion'),
            autor_id=data.get('autor_id')
        )
    

