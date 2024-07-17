from app.dominio.edicion_evento.expositor_repositorio import ExpositorRepositorio

class ExpositorRepositorioImpl(ExpositorRepositorio):
    def __init__(self, db):
        self.db = db

    def crear(self, expositor):
        self.db.expositores.insert_one(expositor.__dict__)

    def obtener(self, id):
        return self.db.expositores.find_one({"id": id})

    def actualizar(self, expositor):
        self.db.expositores.update_one({"id": expositor.id}, {"$set": expositor.__dict__})

    def eliminar(self, id):
        self.db.expositores.delete_one({"id": id})