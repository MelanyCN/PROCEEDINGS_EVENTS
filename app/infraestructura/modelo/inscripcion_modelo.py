from app.infraestructura.extension import db
from app.dominio.edicion_evento.inscripcion import Inscripcion as InscripcionDominio

class InscripcionModelo(db.Model):
    """Modelo de datos para Inscripciones en la base de datos."""

    __tablename__ = 'inscripciones'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    evento_id = db.Column(db.Integer, nullable=False)
    usuario_id = db.Column(db.Integer, nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Convierte la instancia de InscripcionModelo en un diccionario.

        Returns:
            dict: Representación de la inscripción como diccionario.
        """
        return {
            "id": self.id,
            "evento_id": self.evento_id,
            "usuario_id": self.usuario_id,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }

    @staticmethod
    def from_domain(inscripcion_dominio: InscripcionDominio):
        """Crea una instancia de InscripcionModelo desde una entidad de dominio.

        Args:
            inscripcion_dominio (InscripcionDominio): La entidad de dominio de la inscripción.

        Returns:
            InscripcionModelo: La instancia de InscripcionModelo creada.
        """
        return InscripcionModelo(
            id=inscripcion_dominio.id,
            evento_id=inscripcion_dominio.evento_id,
            usuario_id=inscripcion_dominio.usuario_id,
            fecha=inscripcion_dominio.fecha
        )

    def to_domain(self):
        """Convierte la instancia de InscripcionModelo en una entidad de dominio.

        Returns:
            InscripcionDominio: La entidad de dominio de la inscripción.
        """
        return InscripcionDominio(
            id=self.id,
            evento_id=self.evento_id,
            usuario_id=self.usuario_id,
            fecha=self.fecha
        )
