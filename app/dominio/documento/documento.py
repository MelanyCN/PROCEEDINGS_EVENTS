from .autor import Autor

class Documento:
    def __init__(self, id=None, titulo=None, descripcion=None, fecha_publicacion=None, autor=None):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_publicacion = fecha_publicacion
        self.autor = autor

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_publicacion": self.fecha_publicacion.isoformat() if self.fecha_publicacion else None,
            "autor": self.autor.to_dict() if self.autor else None
        }