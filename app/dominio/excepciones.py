
#Autor Exception
class AutorRepositoryError(Exception):
    """Excepción personalizada para errores en el repositorio de autores."""

    def __init__(self, message="Error en el manejo de autores"):
        self.message = message
        super().__init__(self.message)

    pass

#Documento Exception
class DocumentoRepositoryError(Exception):
    """Excepción personalizada para errores en el repositorio de documentos."""
    pass