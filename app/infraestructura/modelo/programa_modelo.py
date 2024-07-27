from app.infraestructura.extension import db
from app.dominio.edicion_evento.programa import Programa as ProgramaDominio

class ProgramaModelo(db.Model):
    """Modelo de datos para Programas en la base de datos."""

    __tablename__ = 'programas'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    evento_id = db.Column(db.Integer, nullable=False)
    nombre = db.Column(db.String(150), nullable=False)
    descripcion = db.Column(db.Text, nullable=True)

    def to_dict(self):
        """Convierte la instancia de ProgramaModelo en un diccionario.

        Returns:
            dict: Representación del programa como diccionario.
        """
        return {
            "id": self.id,
            "evento_id": self.evento_id,
            "nombre": self.nombre,
            "descripcion": self.descripcion
        }

    @staticmethod
    def from_domain(programa_dominio: ProgramaDominio):
        """Crea una instancia de ProgramaModelo desde una entidad de dominio.

        Args:
            programa_dominio (ProgramaDominio): La entidad de dominio del programa.

        Returns:
            ProgramaModelo: La instancia de ProgramaModelo creada.
        """
        return ProgramaModelo(
            id=programa_dominio.id,
            evento_id=programa_dominio.evento_id,
            nombre=programa_dominio.nombre,
            descripcion=programa_dominio.descripcion
        )

    def to_domain(self):
        """Convierte la instancia de ProgramaModelo en una entidad de dominio.

        Returns:
            ProgramaDominio: La entidad de dominio del programa.
        """
        return ProgramaDominio(
            id=self.id,
            evento_id=self.evento_id,
            nombre=self.nombre,
            descripcion=self.descripcion
        )
