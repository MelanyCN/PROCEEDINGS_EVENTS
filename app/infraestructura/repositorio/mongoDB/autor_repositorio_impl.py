from app.dominio.documento.autor_repositorio import AutorRepositorio

class AutorRepositorioImpl(AutorRepositorio):
    def __init__(self, db):
        self.db = db

    def crear(self, autor):
        self.db.autores.insert_one(autor.__dict__)

    def obtener(self, id):
        return self.db.autores.find_one({"id": id})

    def actualizar(self, autor):
        self.db.autores.update_one({"id": autor.id}, {"$set": autor.__dict__})

    def eliminar(self, id):
        self.db.autores.delete_one({"id": id})
