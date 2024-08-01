from app.dominio.documento.autor import AutorRepositorio
from app.infraestructura.modelo.autor_modelo import AutorModelo
from app.infraestructura.extension import db
from app.dominio.excepciones import AutorRepositoryError
from app.dominio.documento.autor import Autor


class AutorRepositorioImpl(AutorRepositorio):
    """
    Implementación del repositorio de autores.
    """

    def __init__(self):
        """
        Inicializa la implementación del repositorio de autores.
        """
        super().__init__()

    def crear(self, autor: Autor):
        """Agrega un nuevo autor a la base de datos."""
        try:
            autor_modelo = AutorModelo(
                nombre=autor.nombre,
                email=autor.email,
                afiliacion=autor.afiliacion,
                nacionalidad=autor.nacionalidad,
                area_interes=autor.area_interes,
                link_foto=autor.link_foto
            )
            db.session.add(autor_modelo)
            db.session.commit()
            # Recupera el ID generado
            autor.id = autor_modelo.id
        except Exception as e:
            db.session.rollback()
            raise RuntimeError(f"Error al crear el autor: {str(e)}")

    def obtener(self, id):
        """
        Obtiene un autor por su identificador.
        
        Args:
            id (int): El identificador del autor.
        
        Returns:
            Optional[AutorDominio]: El autor si existe, de lo contrario None.
        """
        try:
            autor_modelo = AutorModelo.query.get(id)
            return autor_modelo.to_domain() if autor_modelo else None
        except Exception as e:
            raise AutorRepositoryError(f"Error al obtener el autor: {str(e)}")

    def actualizar(self, autor):
        """
        Actualiza un autor existente en la base de datos.
        
        Args:
            autor (AutorDominio): La instancia del autor con la información actualizada.
        """
        try:
            autor_modelo = AutorModelo.query.get(autor.id)
            if autor_modelo:
                autor_modelo.nombre = autor.nombre
                autor_modelo.email = autor.email
                autor_modelo.afiliacion = autor.afiliacion
                autor_modelo.nacionalidad = autor.nacionalidad
                autor_modelo.area_interes = autor.area_interes
                autor_modelo.link_foto = autor.link_foto
                db.session.commit()
            else:
                raise AutorRepositoryError("Autor no encontrado.")
        except Exception as e:
            db.session.rollback()
            raise AutorRepositoryError(f"Error al actualizar el autor: {str(e)}")

    def eliminar(self, id):
        """
        Elimina un autor por su identificador.
        
        Args:
            id (int): El identificador del autor a eliminar.
        """
        try:
            autor_modelo = AutorModelo.query.get(id)
            if autor_modelo:
                db.session.delete(autor_modelo)
                db.session.commit()
            else:
                raise AutorRepositoryError("Autor no encontrado.")
        except Exception as e:
            db.session.rollback()
            raise AutorRepositoryError(f"Error al eliminar el autor: {str(e)}")

    def listar_autores(self):
        """
        Obtiene todos los autores de la base de datos.
        
        Returns:
            list: Una lista de instancias de AutorDominio.
        
        Raises:
            AutorRepositoryError: Si ocurre un error al obtener los autores.
        """
        try:
            autores_modelo = AutorModelo.query.all()
            return [autor.to_domain() for autor in autores_modelo]
        except Exception as e:
            raise AutorRepositoryError(f"Error al listar todos los autores: {e}")
