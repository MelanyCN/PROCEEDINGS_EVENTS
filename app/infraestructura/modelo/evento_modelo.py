from app.infraestructura.extension import db
from app.dominio.evento.evento import Evento as EventoDominio
from app.dominio.evento.edicion import Edicion as EdicionDominio

class EventoModelo(db.Model):
    """Modelo de datos para Eventos en la base de datos."""

    __tablename__ = 'eventos'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    hora = db.Column(db.Time, nullable=True)
    lugar = db.Column(db.String(100), nullable=True)

    edicion_id = db.Column(db.Integer, db.ForeignKey('ediciones.id'), nullable=True)
    edicion = db.relationship('EdicionModelo', back_populates='eventos')

    inscripciones = db.relationship('InscripcionModelo', back_populates='evento', overlaps="evento_inscripcion")
    
    def to_dict(self):
        """Convierte la instancia de EventoModelo en un diccionario.

        Returns:
            dict: Representación del evento como diccionario.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None,
            "descripcion": self.descripcion,
            "hora": self.hora.isoformat() if self.hora else None,
            "lugar": self.lugar,
            "edicion_id": self.edicion_id,
            "edicion": self.edicion.to_dict() if self.edicion else None,
            "inscripciones": [inscripcion.to_dict() for inscripcion in self.inscripciones]
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
            fecha=evento_dominio.fecha,
            descripcion=evento_dominio.descripcion,
            hora=evento_dominio.hora,
            lugar=evento_dominio.lugar,
            edicion_id=evento_dominio.edicion_id
        )

    def to_domain(self):
        """Convierte la instancia de EventoModelo en una entidad de dominio.

        Returns:
            EventoDominio: La entidad de dominio del evento.
        """
        return EventoDominio(
            id=self.id,
            nombre=self.nombre,
            fecha=self.fecha,
            descripcion=self.descripcion,
            hora=self.hora,
            lugar=self.lugar,
            edicion_id=self.edicion_id
        )
