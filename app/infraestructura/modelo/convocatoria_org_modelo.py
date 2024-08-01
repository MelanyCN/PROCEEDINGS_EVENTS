from app.infraestructura.extension import db
from app.dominio.evento.convocatoria_org import ConvocatoriaOrg as ConvocatoriaOrgDominio

# Modelo de datos para Convocatorias de Organización en la base de datos
class ConvocatoriaOrgModelo(db.Model):
    __tablename__ = 'convocatorias_org'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(150), nullable=False)
    fecha = db.Column(db.Date, nullable=False)

    # Clave foránea para la edición
    edicion_id = db.Column(db.Integer, db.ForeignKey('ediciones.id'), nullable=False)
    edicion = db.relationship('EdicionModelo', back_populates='convocatorias_edicion')

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None,
            "edicion_id": self.edicion_id,
            "edicion": self.edicion.to_dict() if self.edicion else None
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
            fecha=convocatoria_org_dominio.fecha,
            edicion_id=convocatoria_org_dominio.edicion_id  # Asegúrate de que este campo esté presente en la entidad de dominio
        )


    def to_domain(self):
        """Convierte la instancia de ConvocatoriaOrgModelo en una entidad de dominio.

        Returns:
            ConvocatoriaOrgDominio: La entidad de dominio de la convocatoria.
        """
        return ConvocatoriaOrgDominio(
            id=self.id,
            nombre=self.nombre,
            fecha=self.fecha,
            edicion_id=self.edicion_id  # Asegúrate de que este campo esté presente en la entidad de dominio
        )

