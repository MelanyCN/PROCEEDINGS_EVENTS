from app.dominio.evento.edicion_repositorio import EdicionRepositorio
from app.infraestructura.modelo.edicion_modelo import EdicionModelo
from app.infraestructura.extension import db

class EdicionRepositorioImpl(EdicionRepositorio):
    """Implementación del repositorio para la entidad Edicion."""

    def __init__(self):
        # Constructor vacío, no se requiere inicialización específica.
        # Este metodo esta intencionalmente vacio
        pass

    def crear(self, edicion: EdicionModelo):
        """Agrega una nueva edición a la base de datos.

        Args:
            edicion (EdicionModelo): La edición a ser agregada.
        """
        try:
            db.session.add(edicion)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al crear la edición: {str(e)}")

    def obtener(self, id: int):
        """Obtiene una edición por su ID.

        Args:
            id (int): ID de la edición a buscar.

        Returns:
            EdicionDominio | None: La edición encontrada o None si no se encuentra.
        """
        try:
            edicion_modelo = EdicionModelo.query.get(id)
            return edicion_modelo.to_domain() if edicion_modelo else None
        except Exception as e:
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al obtener la edición con ID {id}: {str(e)}")

    def actualizar(self, edicion: EdicionModelo):
        """Actualiza una edición existente en la base de datos.

        Args:
            edicion (EdicionModelo): La edición con los datos actualizados.

        Returns:
            EdicionDominio | None: La edición actualizada o None si no se encuentra.
        """
        try:
            edicion_modelo = EdicionModelo.query.get(edicion.id)
            if edicion_modelo:
                edicion_modelo.evento_id = edicion.evento_id
                edicion_modelo.nombre = edicion.nombre
                edicion_modelo.fecha = edicion.fecha
                db.session.commit()
                return edicion_modelo.to_domain()
            return None
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al actualizar la edición: {str(e)}")

    def eliminar(self, id: int):
        """Elimina una edición por su ID.

        Args:
            id (int): ID de la edición a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encuentra la edición.
        """
        try:
            edicion_modelo = EdicionModelo.query.get(id)
            if edicion_modelo:
                db.session.delete(edicion_modelo)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al eliminar la edición con ID {id}: {str(e)}")
