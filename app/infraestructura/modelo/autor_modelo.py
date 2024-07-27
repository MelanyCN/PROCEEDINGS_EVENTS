from app.infraestructura.extension import db
from app.dominio.documento.autor import Autor as AutorDominio

class AutorModelo(db.Model):
    __tablename__ = 'autores'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
        }

    @staticmethod
    def from_domain(autor_dominio: AutorDominio):
        return AutorModelo(
            id=autor_dominio.id,
            nombre=autor_dominio.nombre,
            email=autor_dominio.email
        )

    def to_domain(self):
        return AutorDominio(
            id=self.id,
            nombre=self.nombre,
            email=self.email
        )