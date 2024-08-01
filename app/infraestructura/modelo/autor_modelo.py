from app.infraestructura.extension import db
from app.dominio.documento.autor import Autor as AutorDominio
from app.infraestructura.modelo.documento_modelo import DocumentoModelo

class AutorModelo(db.Model):
    __tablename__ = 'autores'
    
    id_autor = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)
    afiliacion = db.Column(db.String(50), nullable=True)
    nacionalidad = db.Column(db.String(50), nullable=False)
    area_interes = db.Column(db.String(50), nullable=False)
    link_foto = db.Column(db.Text, nullable=False)

    def to_dict(self):
        """
        Convierte la instancia del modelo SQLAlchemy a un diccionario.
        
        Returns:
            dict: Una representación en diccionario de la instancia de AutorModelo.
        """
        return {
            "id_autor": self.id_autor,
            "nombre": self.nombre,
            "email": self.email,
            "afiliacion": self.afiliacion,
            "nacionalidad": self.nacionalidad,
            "area_interes": self.area_interes,
            "link_foto": self.link_foto
        }

    @staticmethod
    def from_domain(autor_dominio: AutorDominio):
        """
        Crea una instancia de AutorModelo a partir de una entidad de dominio AutorDominio.
        
        Args:
            autor_dominio (AutorDominio): La entidad de dominio del autor.
        
        Returns:
            AutorModelo: La instancia del modelo SQLAlchemy de AutorModelo.
        """
        return AutorModelo(
            id_autor=autor_dominio.id_autor,
            nombre=autor_dominio.nombre,
            email=autor_dominio.email,
            afiliacion=autor_dominio.afiliacion,
            nacionalidad=autor_dominio.nacionalidad,
            area_interes=autor_dominio.area_interes,
            link_foto=autor_dominio.link_foto
        )

    def to_domain(self):
        """
        Convierte la instancia de AutorModelo en una entidad de dominio.
        
        Returns:
            AutorDominio: La entidad de dominio del autor.
        """
        return AutorDominio(
            id_autor=self.id_autor,
            nombre=self.nombre,
            email=self.email,
            afiliacion=self.afiliacion,
            nacionalidad=self.nacionalidad,
            area_interes=self.area_interes,
            link_foto=self.link_foto
        )
