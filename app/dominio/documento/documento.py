from .autor import Autor

class Documento:
    def __init__(self, id, titulo, descripcion, fecha_publicacion, autor):
        self.id = id
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_publicacion = fecha_publicacion
        self.autor = Autor