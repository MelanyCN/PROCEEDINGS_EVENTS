from app.dominio.documento.documento_repositorio import DocumentoRepositorio

class DocumentoRepositorioImpl(DocumentoRepositorio):
    def __init__(self, db):
        self.db = db

    def crear(self, documento):
        self.db.documentos.insert_one(documento.__dict__)

    def obtener(self, id):
        return self.db.documentos.find_one({"id": id})

    def actualizar(self, documento):
        self.db.documentos.update_one({"id": documento.id}, {"$set": documento.__dict__})

    def eliminar(self, id):
        self.db.documentos.delete_one({"id": id})
