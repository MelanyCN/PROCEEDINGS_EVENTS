from app.dominio.evento.convocatoria_org import ConvocatoriaOrgRepositorio
from app.infraestructura.modelo.convocatoria_org_modelo import ConvocatoriaOrgModelo
from app.infraestructura.extension import db

class ConvocatoriaOrgRepositorioImpl(ConvocatoriaOrgRepositorio):
    def __init__(self):
        # Constructor de la clase, inicialización si es necesario.
        # Este metodo esta intencionalmente vacio
        pass

    def crear(self, convocatoria_org: ConvocatoriaOrgModelo):
        """Agrega una nueva convocatoria a la base de datos.
        
        Args:
            convocatoria_org (ConvocatoriaOrgModelo): Instancia del modelo ConvocatoriaOrg a persistir.
        """
        try:
            db.session.add(convocatoria_org)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise RuntimeError(f"Error al crear la convocatoria: {str(e)}")

    def obtener(self, id: int):
        """Obtiene una convocatoria de la base de datos por su ID.
        
        Args:
            id (int): ID de la convocatoria a obtener.
            
        Returns:
            ConvocatoriaOrg: Instancia de ConvocatoriaOrg en caso de existir, de lo contrario None.
        """
        try:
            convocatoria_org_modelo = ConvocatoriaOrgModelo.query.get(id)
            return convocatoria_org_modelo.to_domain() if convocatoria_org_modelo else None
        except Exception as e:
            raise RuntimeError(f"Error al obtener la convocatoria con ID {id}: {str(e)}")

    def actualizar(self, convocatoria_org: ConvocatoriaOrgModelo):
        """Actualiza una convocatoria existente en la base de datos.
        
        Args:
            convocatoria_org (ConvocatoriaOrgModelo): Instancia del modelo ConvocatoriaOrg con los nuevos datos.
            
        Returns:
            ConvocatoriaOrg: La convocatoria actualizada en el dominio, o None si no se encontró.
        """
        try:
            convocatoria_org_modelo = ConvocatoriaOrgModelo.query.get(convocatoria_org.id)
            if convocatoria_org_modelo:
                convocatoria_org_modelo.nombre = convocatoria_org.nombre
                convocatoria_org_modelo.fecha = convocatoria_org.fecha
                db.session.commit()
                return convocatoria_org_modelo.to_domain()
            return None
        except Exception as e:
            db.session.rollback()
            raise RuntimeError(f"Error al actualizar la convocatoria: {str(e)}")

    def eliminar(self, id: int):
        """Elimina una convocatoria de la base de datos.
        
        Args:
            id (int): ID de la convocatoria a eliminar.
            
        Returns:
            bool: True si la convocatoria fue eliminada, False si no se encontró.
        """
        try:
            convocatoria_org_modelo = ConvocatoriaOrgModelo.query.get(id)
            if convocatoria_org_modelo:
                db.session.delete(convocatoria_org_modelo)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            raise RuntimeError(f"Error al eliminar la convocatoria con ID {id}: {str(e)}")
