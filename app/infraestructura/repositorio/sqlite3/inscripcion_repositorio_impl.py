from app.dominio.edicion_evento.inscripcion_repositorio import InscripcionRepositorio
from app.dominio.edicion_evento.inscripcion import Inscripcion
from app.infraestructura.extension import db

class InscripcionRepositorioImpl(InscripcionRepositorio):
    def __init__(self):
        # This method is intentionally left empty.
        pass

    def crear(self, inscripcion):
        db.session.add(inscripcion)
        db.session.commit()

    def obtener(self, id):
        return Inscripcion.query.get(id)

    def actualizar(self, inscripcion):
        db.session.commit()

    def eliminar(self, id):
        inscripcion = self.obtener(id)
        if inscripcion:
            db.session.delete(inscripcion)
            db.session.commit()