from app.infraestructura.extension import db
from app.dominio.edicion_evento.evento import Evento as EventoDominio

class EventoModelo(db.Model):
    """Modelo de datos para Eventos en la base de datos."""

    __tablename__ = 'eventos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Convierte la instancia de EventoModelo en un diccionario.

        Returns:
            dict: Representación del evento como diccionario.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }

    @staticmethod
    def from_domain(evento_dominio: EventoDominio):
        """Crea una instancia de EventoModelo desde una entidad de dominio.

        Args:
            evento_dominio (EventoDominio): La entidad de dominio del evento.

        Returns:
            EventoModelo: La instancia de EventoModelo creada.
        """
        return EventoModelo(
            id=evento_dominio.id,
            nombre=evento_dominio.nombre,
            fecha=evento_dominio.fecha
        )

    def to_domain(self):
        """Convierte la instancia de EventoModelo en una entidad de dominio.

        Returns:
            EventoDominio: La entidad de dominio del evento.
        """
        return EventoDominio(
            id=self.id,
            nombre=self.nombre,
            fecha=self.fecha
        )
