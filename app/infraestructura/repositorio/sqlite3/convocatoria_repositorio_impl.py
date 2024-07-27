from app.dominio.edicion_evento.convocatoria_repositorio import ConvocatoriaRepositorio
from app.dominio.edicion_evento.convocatoria_org import ConvocatoriaOrg
from app.infraestructura.extension import db

class ConvocatoriaRepositorioImpl(ConvocatoriaRepositorio):
    def __init__(self):
        # This method is intentionally left empty.
        pass

    def crear(self, convocatoria):
        db.session.add(convocatoria)
        db.session.commit()

    def obtener(self, id):
        return ConvocatoriaOrg.query.get(id)

    def actualizar(self, convocatoria):
        
        db.session.commit()

    def eliminar(self, id):
        convocatoria = self.obtener(id)
        if convocatoria:
            db.session.delete(convocatoria)
            db.session.commit()