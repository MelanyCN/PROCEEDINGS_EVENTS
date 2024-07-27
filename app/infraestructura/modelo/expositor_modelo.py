from app.infraestructura.extension import db
from app.dominio.edicion_evento.expositor import Expositor as ExpositorDominio

class ExpositorModelo(db.Model):
    """Modelo de datos para Expositores en la base de datos."""

    __tablename__ = 'expositores'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), nullable=False, unique=True)

    def to_dict(self):
        """Convierte la instancia de ExpositorModelo en un diccionario.

        Returns:
            dict: Representación del expositor como diccionario.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email
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
            email=expositor_dominio.email
        )

    def to_domain(self):
        """Convierte la instancia de ExpositorModelo en una entidad de dominio.

        Returns:
            ExpositorDominio: La entidad de dominio del expositor.
        """
        return ExpositorDominio(
            id=self.id,
            nombre=self.nombre,
            email=self.email
        )
