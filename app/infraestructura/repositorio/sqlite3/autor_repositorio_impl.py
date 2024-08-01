from app.dominio.documento.autor import AutorRepositorio
from app.infraestructura.modelo.autor_modelo import AutorModelo
from app.infraestructura.extension import db
from app.dominio.excepciones import AutorRepositoryError

class AutorRepositorioImpl(AutorRepositorio):
    """
    Implementación del repositorio de autores.
    """

    def __init__(self):
        """
        Inicializa la implementación del repositorio de autores.
        """
        super().__init__()


    def crear_autor(self, autor):
        """
        Crea un nuevo autor en la base de datos.
        
        Args:
            autor (AutorDominio): La instancia del autor a crear.
        """
        try:
            autor_modelo = AutorModelo.from_domain(autor)
            db.session.add(autor_modelo)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise AutorRepositoryError(f"Error al crear el autor: {str(e)}")


    def obtener_autor(self, id):
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


    def actualizar_autor(self, autor):
        """
        Actualiza un autor existente en la base de datos.
        
        Args:
            autor (AutorDominio): La instancia del autor con la información actualizada.
        """
        try:
            autor_modelo = AutorModelo.query.get(autor.id)
            if autor_modelo:
                autor_modelo.nombre = autor.nombre
                autor_modelo.biografia = autor.biografia
                db.session.commit()
            else:
                raise AutorRepositoryError("Autor no encontrado.")
        except Exception as e:
            db.session.rollback()
            raise AutorRepositoryError(f"Error al actualizar el autor: {str(e)}")


    def eliminar_autor(self, id):
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


    def listar_autores(self, id_documento):
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