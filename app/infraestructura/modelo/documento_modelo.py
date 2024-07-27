from app.infraestructura.extension import db
from app.dominio.documento.documento import Documento as DocumentoDominio

class DocumentoModelo(db.Model):
    __tablename__ = 'documentos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_publicacion = db.Column(db.Date, nullable=True)
    autor_id = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_publicacion": self.fecha_publicacion.isoformat() if self.fecha_publicacion else None,
            "autor_id": self.autor_id
        }

    @staticmethod
    def from_domain(documento_dominio: DocumentoDominio):
        return DocumentoModelo(
            id=documento_dominio.id,
            titulo=documento_dominio.titulo,
            descripcion=documento_dominio.descripcion,
            fecha_publicacion=documento_dominio.fecha_publicacion,
            autor_id=documento_dominio.autor.id
        )

    def to_domain(self):
        return DocumentoDominio(
            id=self.id,
            titulo=self.titulo,
            descripcion=self.descripcion,
            fecha_publicacion=self.fecha_publicacion,
            autor=None
        )