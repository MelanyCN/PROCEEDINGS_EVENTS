from app.infraestructura.extension import db
from app.dominio.evento.expositor import Expositor as ExpositorDominio

class ExpositorModelo(db.Model):
    """Modelo de datos para Expositores en la base de datos."""

    __tablename__ = 'expositores'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    apellido = db.Column(db.String(150), nullable=False)
    ocupacion = db.Column(db.String(150), nullable=True)
    email = db.Column(db.String(150), nullable=False, unique=True)
    img_perfil_url = db.Column(db.String(255), nullable=True)
    trayectoria_academica = db.Column(db.Text, nullable=True)

    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'), nullable=False)
    evento = db.relationship('EventoModelo', backref=db.backref('expositores', lazy=True))

    def to_dict(self):
        """Convierte la instancia de ExpositorModelo en un diccionario.

        Returns:
            dict: Representación del expositor como diccionario.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "ocupacion": self.ocupacion,
            "email": self.email,
            "img_perfil_url": self.img_perfil_url,
            "trayectoria_academica": self.trayectoria_academica,
            "evento_id": self.evento_id
        }

    @staticmethod
    def from_domain(expositor_dominio: ExpositorDominio):
        """Crea una instancia de ExpositorModelo desde una entidad de dominio.

        Args:
            expositor_dominio (ExpositorDominio): La entidad de dominio del expositor.

        Returns:
            ExpositorModelo: La instancia de ExpositorModelo creada.
        """
        return ExpositorModelo(
            id=expositor_dominio.id,
            nombre=expositor_dominio.nombre,
            apellido=expositor_dominio.apellido,
            ocupacion=expositor_dominio.ocupacion,
            email=expositor_dominio.email,
            img_perfil_url=expositor_dominio.img_perfil_url,
            trayectoria_academica=expositor_dominio.trayectoria_academica,
            evento_id=expositor_dominio.evento_id
        )

    def to_domain(self):
        """Convierte la instancia de ExpositorModelo en una entidad de dominio.

        Returns:
            ExpositorDominio: La entidad de dominio del expositor.
        """
        return ExpositorDominio(
            id=self.id,
            nombre=self.nombre,
            apellido=self.apellido,
            ocupacion=self.ocupacion,
            email=self.email,
            img_perfil_url=self.img_perfil_url,
            trayectoria_academica=self.trayectoria_academica,
            evento_id=self.evento_id
        )