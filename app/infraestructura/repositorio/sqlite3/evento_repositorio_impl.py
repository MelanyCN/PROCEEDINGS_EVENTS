from app.dominio.edicion_evento.evento_repositorio import EventoRepositorio
from app.dominio.edicion_evento.evento import Evento
from app.infraestructura.extension import db

class EventoRepositorioImpl(EventoRepositorio):
    def __init__(self):
        # This method is intentionally left empty.
        pass

    def crear(self, evento):
        db.session.add(evento)
        db.session.commit()

    def obtener(self, id):
        return Evento.query.get(id)

    def actualizar(self, evento):
        db.session.commit()

    def eliminar(self, id):
        evento = self.obtener(id)
        if evento:
            db.session.delete(evento)
            db.session.commit()