from app.dominio.edicion_evento.convocatoria_repositorio import ConvocatoriaRepositorio

class ConvocatoriaRepositorioImpl(ConvocatoriaRepositorio):
    def __init__(self, db):
        self.db = db

    def crear(self, convocatoria):
        self.db.convocatorias.insert_one(convocatoria.__dict__)

    def obtener(self, id):
        return self.db.convocatorias.find_one({"id": id})

    def actualizar(self, convocatoria):
        self.db.convocatorias.update_one({"id": convocatoria.id}, {"$set": convocatoria.__dict__})

    def eliminar(self, id):
        self.db.convocatorias.delete_one({"id": id})