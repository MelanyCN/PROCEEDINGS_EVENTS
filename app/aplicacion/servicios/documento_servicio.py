from abc import ABC, abstractmethod
from typing import Optional, List
from app.dominio.documento.documento import Documento as DocumentoDominio
from app.dominio.excepciones import DocumentoRepositoryError

class DocumentoServicio(ABC):
    """
    Interfaz abstracta para las operaciones del controlador de documentos.
    Define los métodos que deben ser implementados para gestionar documentos.
    """

    @abstractmethod
    def crear_documento(self, documento: DocumentoDominio):
        """
        Crea un nuevo documento.

        Args:
            documento (DocumentoDominio): El documento a crear.
        """
        pass

    @abstractmethod
    def obtener_documento(self, id_documento: int) -> DocumentoDominio:
        """
        Obtiene un documento por su identificador.

        Args:
            id_documento (int): El identificador del documento.

        Returns:
            Optional[DocumentoDominio]: El documento si existe, de lo contrario None.
        """
        pass

    @abstractmethod
    def actualizar_documento(self, documento: DocumentoDominio):
        """
        Actualiza un documento existente.

        Args:
            documento (DocumentoDominio): El documento con la información actualizada.
        """
        pass

    @abstractmethod
    def eliminar_documento(self, id_documento: int):
        """
        Elimina un documento por su identificador.

        Args:
            id_documento (int): El identificador del documento a eliminar.
        """
        pass

    @abstractmethod
    async def listar_documentos(self, busqueda: Optional[str] = None) -> Optional[List[DocumentoDominio]]:
        """
        Lista documentos que coinciden con los criterios de búsqueda.

        Args:
            busqueda (Optional[str]): Un término de búsqueda para filtrar documentos.

        Returns:
            List[DocumentoDominio]: Lista de documentos que coinciden con la búsqueda.
        """
        pass


class DocumentoServicioImpl(DocumentoServicio):
    """
    Implementación concreta del controlador de documentos.
    Gestiona las operaciones relacionadas con documentos utilizando un repositorio.
    """

    def __init__(self, documento_repo):
        """
        Inicializa el controlador con el repositorio de documentos.

        Args:
            documento_repo (DocumentoRepositorio): Repositorio para la gestión de documentos.
        """
        self.documento_repo = documento_repo

    def crear_documento(self, documento: DocumentoDominio) -> None:
        try:
            self.documento_repo.crear(documento)
        except Exception as ex:
            raise DocumentoRepositoryError(f"Error al crear documento: {str(ex)}")

    def obtener_documento(self, id_documento: int) -> Optional[DocumentoDominio]:
        try:
            return self.documento_repo.obtener(id_documento)
        except Exception as ex:
            raise DocumentoRepositoryError(f"Error al obtener el documento: {str(ex)}")

    def actualizar_documento(self, documento: DocumentoDominio) -> None:
        try:
            self.documento_repo.actualizar(documento)
        except Exception as ex:
            raise DocumentoRepositoryError(f"Error al actualizar el documento: {str(ex)}")

    def eliminar_documento(self, id_documento: int) -> None:
        try:
            self.documento_repo.eliminar(id_documento)
        except Exception as ex:
            raise DocumentoRepositoryError(f"Error al eliminar el documento: {str(ex)}")

    async def listar_documentos(self, busqueda: Optional[str] = None) -> List[DocumentoDominio]:
        try:
            return await self.documento_repo.listar(busqueda)
        except Exception as ex:
            raise DocumentoRepositoryError(f"Error al listar documentos: {str(ex)}")
