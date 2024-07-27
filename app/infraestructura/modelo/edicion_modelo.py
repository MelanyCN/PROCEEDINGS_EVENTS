from app.infraestructura.extension import db
from app.dominio.edicion.edicion import Edicion as EdicionDominio
from datetime import datetime

class EdicionModelo(db.Model):
    """Modelo de datos para Ediciones en la base de datos."""

    __tablename__ = 'ediciones'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    evento_id = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(150), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Convierte la instancia de EdicionModelo en un diccionario.

        Returns:
            dict: Representación de la edición como diccionario.
        """
        return {
            "id": self.id,
            "evento_id": self.evento_id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }

    @staticmethod
    def from_domain(edicion_dominio: EdicionDominio):
        """Crea una instancia de EdicionModelo desde una entidad de dominio.

        Args:
            edicion_dominio (EdicionDominio): La entidad de dominio de la edición.

        Returns:
            EdicionModelo: La instancia de EdicionModelo creada.
        """
        return EdicionModelo(
            id=edicion_dominio.id,
            evento_id=edicion_dominio.evento_id,
            nombre=edicion_dominio.nombre,
            fecha=edicion_dominio.fecha
        )

    def to_domain(self):
        """Convierte la instancia de EdicionModelo en una entidad de dominio.

        Returns:
            EdicionDominio: La entidad de dominio de la edición.
        """
        return EdicionDominio(
            id=self.id,
            evento_id=self.evento_id,
            nombre=self.nombre,
            fecha=self.fecha
        )
