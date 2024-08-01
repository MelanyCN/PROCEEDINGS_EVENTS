from app.infraestructura.extension import db
from app.dominio.evento.inscripcion import Inscripcion as InscripcionDominio

class InscripcionModelo(db.Model):
    """Modelo de datos para Inscripciones en la base de datos."""

    __tablename__ = 'inscripciones'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    apellidos = db.Column(db.String(800), nullable=False)
    dni = db.Column(db.Integer, nullable=False)
    ocupacion = db.Column(db.String(50), nullable=False)
    correo = db.Column(db.String(50), nullable=False)
    vaucher_url = db.Column(db.String(200), nullable=False)

    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'), nullable=False)
    evento = db.relationship('EventoModelo', back_populates='inscripciones', overlaps="inscripciones_evento")
    
    def to_dict(self):
        """Convierte la instancia de InscripcionModelo en un diccionario.

        Returns:
            dict: Representación de la inscripción como diccionario.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "apellidos": self.apellidos,
            "dni": self.dni,
            "ocupacion": self.ocupacion,
            "correo": self.correo,
            "vaucher_url": self.vaucher_url,
            "evento_id": self.evento_id
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
            nombre=inscripcion_dominio.nombre,
            apellidos=inscripcion_dominio.apellidos,
            dni=inscripcion_dominio.dni,
            ocupacion=inscripcion_dominio.ocupacion,
            correo=inscripcion_dominio.correo,
            vaucher_url=inscripcion_dominio.vaucher_url,
            evento_id=inscripcion_dominio.evento_id
        )

    def to_domain(self):
        """Convierte la instancia de InscripcionModelo en una entidad de dominio.

        Returns:
            InscripcionDominio: La entidad de dominio de la inscripción.
        """
        return InscripcionDominio(
            id=self.id,
            nombre=self.nombre,
            apellidos=self.apellidos,
            dni=self.dni,
            ocupacion=self.ocupacion,
            correo=self.correo,
            vaucher_url=self.vaucher_url,
            evento_id=self.evento_id
        )
