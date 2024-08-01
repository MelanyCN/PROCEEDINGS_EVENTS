from abc import ABC, abstractmethod
from typing import Optional, List
from app.dominio.documento.autor import Autor as AutorDominio
from app.dominio.excepciones import AutorRepositoryError

class AutorServicio(ABC):
    """
    Interfaz abstracta para las operaciones del controlador de autores.
    Define los métodos que deben ser implementados para gestionar autores.
    """

    @abstractmethod
    def crear_autor(self, autor: AutorDominio):
        """
        Crea un nuevo autor.

        Args:
            autor (AutorDominio): El autor a crear.
        """
        pass

    @abstractmethod
    def obtener_autor(self, id_autor: int) -> AutorDominio:
        """
        Obtiene un autor por su identificador.

        Args:
            id_autor (int): El identificador del autor.

        Returns:
            Optional[AutorDominio]: El autor si existe, de lo contrario None.
        """
        pass

    @abstractmethod
    def actualizar_autor(self, autor: AutorDominio):
        """
        Actualiza un autor existente.

        Args:
            autor (AutorDominio): El autor con la información actualizada.
        """
        pass

    @abstractmethod
    def eliminar_autor(self, id_autor: int):
        """
        Elimina un autor por su identificador.

        Args:
            id_autor (int): El identificador del autor a eliminar.
        """
        pass

    @abstractmethod
    async def listar_autores(self) -> Optional[List[AutorDominio]]:
        """
        Lista todos los autores.

        Returns:
            List[AutorDominio]: Lista de todos los autores.
        """
        pass

    @abstractmethod
    async def listar_autores_por_documento(self, id_documento: int) -> Optional[List[AutorDominio]]:
        """
        Lista los autores pertenecientes a un documento específico.

        Args:
            id_documento (int): El identificador del documento.

        Returns:
            Optional[List[AutorDominio]]: Lista de autores si existen, de lo contrario None.
        """
        pass


class AutorServicioImpl(AutorServicio):
    """
    Implementación concreta del controlador de autores.
    Gestiona las operaciones relacionadas con autores utilizando un repositorio.
    """

    def __init__(self, autor_repo):
        """
        Inicializa el controlador con el repositorio de autores.

        Args:
            autor_repo (AutorRepositorio): Repositorio para la gestión de autores.
        """
        self.autor_repo = autor_repo

    def crear_autor(self, autor: AutorDominio) -> None:
        try:
            self.autor_repo.crear(autor)
        except Exception as ex:
            raise AutorRepositoryError(f"Error al crear autor: {str(ex)}")

    def obtener_autor(self, id_autor: int) -> Optional[AutorDominio]:
        try:
            return self.autor_repo.obtener(id_autor)
        except Exception as ex:
            raise AutorRepositoryError(f"Error al obtener el autor: {str(ex)}")

    def actualizar_autor(self, autor: AutorDominio) -> None:
        try:
            self.autor_repo.actualizar(autor)
        except Exception as ex:
            raise AutorRepositoryError(f"Error al actualizar el autor: {str(ex)}")

    def eliminar_autor(self, id_autor: int) -> None:
        try:
            self.autor_repo.eliminar(id_autor)
        except Exception as ex:
            raise AutorRepositoryError(f"Error al eliminar el autor: {str(ex)}")

    async def listar_autores(self) -> List[AutorDominio]:
        try:
            return await self.autor_repo.listar()
        except Exception as ex:
            raise AutorRepositoryError(f"Error al listar autores: {str(ex)}")

    async def listar_autores_por_documento(self, id_documento: int) -> List[AutorDominio]:
        try:
            return await self.autor_repo.listar_por_documento(id_documento)
        except Exception as ex:
            raise AutorRepositoryError(f"Error al listar autores por documento: {str(ex)}")
