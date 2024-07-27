from app.dominio.edicion_evento.expositor_repositorio import ExpositorRepositorio
from app.dominio.edicion_evento.expositor import Expositor
from app.infraestructura.extension import db

class ExpositorRepositorioImpl(ExpositorRepositorio):
    def __init__(self):
        # This method is intentionally left empty.
        pass

    def crear(self, expositor):
        db.session.add(expositor)
        db.session.commit()

    def obtener(self, id):
        return Expositor.query.get(id)

    def actualizar(self, expositor):
        db.session.commit()

    def eliminar(self, id):
        expositor = self.obtener(id)
        if expositor:
            db.session.delete(expositor)
            db.session.commit()