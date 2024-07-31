from app.dominio.evento.programa_repositorio import ProgramaRepositorio
from app.infraestructura.modelo.programa_modelo import ProgramaModelo
from app.infraestructura.extension import db

class ProgramaRepositorioImpl(ProgramaRepositorio):
    """Implementación del repositorio para la entidad Programa."""

    def __init__(self):
        # Constructor vacío, no se requiere inicialización específica.
        pass

    def crear(self, programa: ProgramaModelo):
        """Agrega un nuevo programa a la base de datos.

        Args:
            programa (ProgramaModelo): El programa a ser agregado.
        """
        try:
            db.session.add(programa)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al crear el programa: {str(e)}")

    def obtener(self, id: int):
        """Obtiene un programa por su ID.

        Args:
            id (int): El ID del programa a buscar.

        Returns:
            ProgramaModelo | None: El programa encontrado o None si no se encuentra.
        """
        try:
            programa_modelo = ProgramaModelo.query.get(id)
            return programa_modelo.to_domain() if programa_modelo else None
        except Exception as e:
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al obtener el programa con ID {id}: {str(e)}")

    def actualizar(self, programa: ProgramaModelo):
        """Actualiza un programa existente en la base de datos.

        Args:
            programa (ProgramaModelo): El programa con los datos actualizados.

        Returns:
            ProgramaModelo | None: El programa actualizado o None si no se encuentra.
        """
        try:
            programa_modelo = ProgramaModelo.query.get(programa.id)
            if programa_modelo:
                programa_modelo.evento_id = programa.evento_id
                programa_modelo.nombre = programa.nombre
                programa_modelo.descripcion = programa.descripcion
                db.session.commit()
                return programa_modelo.to_domain()
            return None
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al actualizar el programa: {str(e)}")

    def eliminar(self, id: int):
        """Elimina un programa de la base de datos por su ID.

        Args:
            id (int): El ID del programa a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encuentra el programa.
        """
        try:
            programa_modelo = ProgramaModelo.query.get(id)
            if programa_modelo:
                db.session.delete(programa_modelo)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al eliminar el programa con ID {id}: {str(e)}")
