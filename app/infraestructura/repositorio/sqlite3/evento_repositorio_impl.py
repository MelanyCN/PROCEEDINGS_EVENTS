from app.dominio.evento.evento import EventoRepositorio
from app.infraestructura.modelo.evento_modelo import EventoModelo
from app.infraestructura.extension import db

class EventoRepositorioImpl(EventoRepositorio):
    """Implementación del repositorio para la entidad Evento."""

    def __init__(self):
        # Constructor vacío, no se requiere inicialización específica.
        pass

    def crear(self, evento: EventoModelo):
        """Agrega un nuevo evento a la base de datos.

        Args:
            evento (EventoModelo): El evento a ser agregado.
        """
        try:
            db.session.add(evento)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al crear el evento: {str(e)}")

    def obtener(self, id: int):
        """Obtiene un evento por su ID.

        Args:
            id (int): El ID del evento a buscar.

        Returns:
            EventoModelo | None: El evento encontrado o None si no se encuentra.
        """
        try:
            evento_modelo = EventoModelo.query.get(id)
            return evento_modelo.to_domain() if evento_modelo else None
        except Exception as e:
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al obtener el evento con ID {id}: {str(e)}")

    def actualizar(self, evento: EventoModelo):
        """Actualiza un evento existente en la base de datos.

        Args:
            evento (EventoModelo): El evento con los datos actualizados.

        Returns:
            EventoModelo | None: El evento actualizado o None si no se encuentra.
        """
        try:
            evento_modelo = EventoModelo.query.get(evento.id)
            if evento_modelo:
                evento_modelo.nombre = evento.nombre
                evento_modelo.fecha = evento.fecha
                evento_modelo.lugar = evento.lugar
                evento_modelo.descripcion = evento.descripcion
                evento_modelo.hora = evento.hora
                db.session.commit()
                return evento_modelo.to_domain()
            return None
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al actualizar el evento: {str(e)}")

    def eliminar(self, id: int):
        """Elimina un evento de la base de datos por su ID.

        Args:
            id (int): El ID del evento a eliminar.

        Returns:
            bool: True si la eliminación fue exitosa, False si no se encuentra el evento.
        """
        try:
            evento_modelo = EventoModelo.query.get(id)
            if evento_modelo:
                db.session.delete(evento_modelo)
                db.session.commit()
                return True
            return False
        except Exception as e:
            db.session.rollback()
            # Log o manejo del error según sea necesario.
            raise RuntimeError(f"Error al eliminar el evento con ID {id}: {str(e)}")
