from app.infraestructura.extension import db
from app.dominio.documento.documento import Documento as DocumentoDominio

class DocumentoModelo(db.Model):
    __tablename__ = 'documentos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)
    fecha_publicacion = db.Column(db.Date, nullable=True)
    link_imagen = db.Column(db.Text, nullable=False)
    link_documento = db.Column(db.Text, nullable=False)
    autor_id = db.Column(db.Integer, db.ForeignKey('autores.id_autor'), nullable=False)
    
    autor = db.relationship('AutorModelo', backref=db.backref('documentos', lazy=True))

    @staticmethod
    def to_dict(self):
        """
        Convierte la instancia del modelo SQLAlchemy a un diccionario. 
        
        Returns:
            dict: Una representación en diccionario de la instancia de DocumentoModelo.
        """
        return {
            "id": self.id,
            "titulo": self.titulo,
            "descripcion": self.descripcion,
            "fecha_publicacion": self.fecha_publicacion.isoformat() if self.fecha_publicacion else None,
            "link_imagen": self.link_imagen,
            "link_documento": self.link_documento,
            "autor_id": self.autor_id
        }
    
    def to_domain(self):
        """
        Convierte la instancia de DocumentoModelo en una entidad de dominio.
        
        Returns:
            DocumentoDominio: La entidad de dominio del documento.
        """
        return DocumentoDominio(
            id=self.id,
            titulo=self.titulo,
            descripcion=self.descripcion,
            fecha_publicacion=self.fecha_publicacion,
            link_imagen=self.link_imagen,
            link_documento=self.link_documento,
            autor_id=self.autor_id
        )

