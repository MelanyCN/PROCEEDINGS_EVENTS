from app.dominio.edicion_evento.expositor_repositorio import ExpositorRepositorio
from app.infraestructura.modelo.expositor_modelo import ExpositorModelo
from app.infraestructura.extension import db

class ExpositorRepositorioImpl(ExpositorRepositorio):
    """Implementación del repositorio para la entidad Expositor."""

    def __init__(self):
        # Constructor vacío, no se requiere inicialización específica.
        # Este metodo esta intencionalmente vacio
        pass

    def crear(self, expositor: ExpositorModelo):
        """Agrega un nuevo expositor a la base de datos.

        Args:
            expositor (ExpositorModelo): El expositor a ser agregado.
        """
        try:
            db.session.add(expositor)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al crear el expositor: {str(e)}")

    def obtener(self, id: int):
        """Obtiene un expositor por su ID.

        Args:
            id (int): El ID del expositor a buscar.

        Returns:
            ExpositorModelo | None: El expositor encontrado o None si no se encuentra.
        """
        try:
            expositor_modelo = ExpositorModelo.query.get(id)
            return expositor_modelo.to_domain() if expositor_modelo else None
        except Exception as e:
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al obtener el expositor con ID {id}: {str(e)}")

    def actualizar(self, expositor: ExpositorModelo):
        """Actualiza un expositor existente en la base de datos.

        Args:
            expositor (ExpositorModelo): El expositor con los datos actualizados.

        Returns:
            ExpositorModelo | None: El expositor actualizado o None si no se encuentra.
        """
        try:
            expositor_modelo = ExpositorModelo.query.get(expositor.id)
            if expositor_modelo:
                expositor_modelo.nombre = expositor.nombre
                expositor_modelo.email = expositor.email
                db.session.commit()
                return expositor_modelo.to_domain()
            return None
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al actualizar el expositor: {str(e)}")

    def eliminar(self, id: int):
        """Elimina un expositor de la base de datos por su ID.

        Args:
            id (int): El ID del expositor a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encuentra el expositor.
        """
        try:
            expositor_modelo = ExpositorModelo.query.get(id)
            if expositor_modelo:
                db.session.delete(expositor_modelo)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al eliminar el expositor con ID {id}: {str(e)}")
