from app.aplicacion.controller.documento_controller import DocumentoController

class DocumentoControllerImpl(DocumentoController):
    def __init__(self, documento_repo):
        self.documento_repo = documento_repo

    def crear_documento(self, documento):
        return self.documento_repo.crear(documento)

    def obtener_documento(self, id):
        return self.documento_repo.obtener(id)

    def actualizar_documento(self, documento):
        return self.documento_repo.actualizar(documento)

    def eliminar_documento(self, id):
        return self.documento_repo.eliminar(id)