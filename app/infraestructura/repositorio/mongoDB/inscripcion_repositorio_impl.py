from app.dominio.edicion_evento.inscripcion_repositorio import InscripcionRepositorio

class InscripcionRepositorioImpl(InscripcionRepositorio):
    def __init__(self, db):
        self.db = db

    def crear(self, inscripcion):
        self.db.inscripciones.insert_one(inscripcion.__dict__)

    def obtener(self, id):
        return self.db.inscripciones.find_one({"id": id})

    def actualizar(self, inscripcion):
        self.db.inscripciones.update_one({"id": inscripcion.id}, {"$set": inscripcion.__dict__})

    def eliminar(self, id):
        self.db.inscripciones.delete_one({"id": id})