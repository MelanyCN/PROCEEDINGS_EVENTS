from app.dominio.documento.documento_repositorio import DocumentoRepositorio
from app.infraestructura.modelo.documento_modelo import DocumentoModelo
from app.infraestructura.extension import db

class DocumentoRepositorioImpl(DocumentoRepositorio):
    def __init__(self):
        # This method is intentionally left empty.
        pass

    def crear(self, documento):
        documento_modelo = DocumentoModelo.from_domain(documento)
        db.session.add(documento_modelo)
        db.session.commit()

    def obtener(self, id):
        documento_modelo = DocumentoModelo.query.get(id)
        return documento_modelo.to_domain() if documento_modelo else None

    def actualizar(self, documento):
        documento_modelo = DocumentoModelo.query.get(documento.id)
        if documento_modelo:
            documento_modelo.titulo = documento.titulo
            documento_modelo.descripcion = documento.descripcion
            documento_modelo.fecha_publicacion = documento.fecha_publicacion
            db.session.commit()

    def eliminar(self, id):
        documento_modelo = DocumentoModelo.query.get(id)
        if documento_modelo:
            db.session.delete(documento_modelo)
            db.session.commit()