from app.infraestructura.extension import db
from app.dominio.documento.autor import Autor as AutorDominio

class AutorModelo(db.Model):
    __tablename__ = 'autores'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    afiliacion = db.Column(db.String(50), nullable=True)
    nacionalidad = db.Column(db.String(50), nullable=False)
    area_interes = db.Column(db.String(50), nullable=False)
    link_foto = db.Column(db.Text, nullable=False)

    documentos = db.relationship('DocumentoModelo', back_populates='autor')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
            "afiliacion": self.afiliacion,
            "nacionalidad": self.nacionalidad,
            "area_interes": self.area_interes,
            "link_foto": self.link_foto,
            "documentos": [documento.to_dict() for documento in self.documentos]
        }

    @staticmethod
    def from_domain(autor_dominio: AutorDominio):
        return AutorModelo(
            id=autor_dominio.id,
            nombre=autor_dominio.nombre,
            email=autor_dominio.email,
            afiliacion=autor_dominio.afiliacion,
            nacionalidad=autor_dominio.nacionalidad,
            area_interes=autor_dominio.area_interes,
            link_foto=autor_dominio.link_foto
        )

    def to_domain(self):
        return AutorDominio(
            id=self.id,
            nombre=self.nombre,
            email=self.email,
            afiliacion=self.afiliacion,
            nacionalidad=self.nacionalidad,
            area_interes=self.area_interes,
            link_foto=self.link_foto
        )
