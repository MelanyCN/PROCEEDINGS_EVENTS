from app.dominio.evento.inscripcion import InscripcionRepositorio
from app.infraestructura.modelo.inscripcion_modelo import InscripcionModelo
from app.infraestructura.extension import db

class InscripcionRepositorioImpl(InscripcionRepositorio):
    """Implementación del repositorio para la entidad Inscripcion."""

    def __init__(self):
        # Constructor vacío, no se requiere inicialización específica.
        pass

    def crear(self, inscripcion: InscripcionModelo):
        """Agrega una nueva inscripción a la base de datos.

        Args:
            inscripcion (InscripcionModelo): La inscripción a ser agregada.
        """
        try:
            db.session.add(inscripcion)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al crear la inscripción: {str(e)}")

    def obtener(self, id: int):
        """Obtiene una inscripción por su ID.

        Args:
            id (int): El ID de la inscripción a buscar.

        Returns:
            InscripcionModelo | None: La inscripción encontrada o None si no se encuentra.
        """
        try:
            inscripcion_modelo = InscripcionModelo.query.get(id)
            return inscripcion_modelo.to_domain() if inscripcion_modelo else None
        except Exception as e:
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al obtener la inscripción con ID {id}: {str(e)}")

    def actualizar(self, inscripcion: InscripcionModelo):
        """Actualiza una inscripción existente en la base de datos.

        Args:
            inscripcion (InscripcionModelo): La inscripción con los datos actualizados.

        Returns:
            InscripcionModelo | None: La inscripción actualizada o None si no se encuentra.
        """
        try:
            inscripcion_modelo = InscripcionModelo.query.get(inscripcion.id)
            if inscripcion_modelo:
                inscripcion_modelo.nombre = inscripcion.nombre
                inscripcion_modelo.apellidos = inscripcion.apellidos
                inscripcion_modelo.dni = inscripcion.dni
                inscripcion_modelo.ocupacion = inscripcion.ocupacion
                inscripcion_modelo.correo = inscripcion.correo
                inscripcion_modelo.vaucher_url = inscripcion.vaucher_url
                inscripcion_modelo.evento_id = inscripcion.evento_id
                db.session.commit()
                return inscripcion_modelo.to_domain()
            return None
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al actualizar la inscripción: {str(e)}")

    def eliminar(self, id: int):
        """Elimina una inscripción por su ID.

        Args:
            id (int): El ID de la inscripción a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encuentra la inscripción.
        """
        try:
            inscripcion_modelo = InscripcionModelo.query.get(id)
            if inscripcion_modelo:
                db.session.delete(inscripcion_modelo)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al eliminar la inscripción con ID {id}: {str(e)}")