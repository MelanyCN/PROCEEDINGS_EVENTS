from app.infraestructura.extension import db
from app.dominio.evento.convocatoria_org import ConvocatoriaOrg as ConvocatoriaOrgDominio

class ConvocatoriaOrgModelo(db.Model):
    """Modelo de datos para Convocatorias de Organización en la base de datos."""

    __tablename__ = 'convocatorias_org'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    def to_dict(self):
        """Convierte la instancia de ConvocatoriaOrgModelo en un diccionario.

        Returns:
            dict: Representación de la convocatoria como diccionario.
        """
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }

    @staticmethod
    def from_domain(convocatoria_org_dominio: ConvocatoriaOrgDominio):
        """Crea una instancia de ConvocatoriaOrgModelo desde una entidad de dominio.

        Args:
            convocatoria_org_dominio (ConvocatoriaOrgDominio): La entidad de dominio de la convocatoria.

        Returns:
            ConvocatoriaOrgModelo: La instancia de ConvocatoriaOrgModelo creada.
        """
        return ConvocatoriaOrgModelo(
            id=convocatoria_org_dominio.id,
            nombre=convocatoria_org_dominio.nombre,
            fecha=convocatoria_org_dominio.fecha
        )

    def to_domain(self):
        """Convierte la instancia de ConvocatoriaOrgModelo en una entidad de dominio.

        Returns:
            ConvocatoriaOrgDominio: La entidad de dominio de la convocatoria.
        """
        return ConvocatoriaOrgDominio(
            id=self.id,
            nombre=self.nombre,
            fecha=self.fecha
        )
