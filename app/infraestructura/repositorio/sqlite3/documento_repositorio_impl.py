from app.dominio.documento.documento import DocumentoRepositorio, Documento
from app.infraestructura.modelo.documento_modelo import DocumentoModelo
from app.infraestructura.extension import db
from typing import List

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

    def listar(self) -> List[Documento]:
        """
        Lista todos los documentos en la base de datos.

        Returns:
            List[Documento]: Lista de todos los documentos como objetos del dominio.
        """
        documentos_modelo = DocumentoModelo.query.all()
        return [documento_modelo.to_domain() for documento_modelo in documentos_modelo]