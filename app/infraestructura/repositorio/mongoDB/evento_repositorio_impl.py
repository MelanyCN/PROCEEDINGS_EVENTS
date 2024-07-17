from app.dominio.edicion_evento.evento_repositorio import EventoRepositorio

class EventoRepositorioImpl(EventoRepositorio):
    def __init__(self, db):
        self.db = db

    def crear(self, evento):
        self.db.eventos.insert_one(evento.__dict__)

    def obtener(self, id):
        return self.db.eventos.find_one({"id": id})

    def actualizar(self, evento):
        self.db.eventos.update_one({"id": evento.id}, {"$set": evento.__dict__})

    def eliminar(self, id):
        self.db.eventos.delete_one({"id": id})