from app.dominio.evento.edicion import Edicion
from app.dominio.evento.edicion_repositorio import EdicionRepositorio
from app.aplicacion.controller.edicion_controller import EdicionController

# Implementación del controlador de ediciones
class EdicionControllerImpl(EdicionController):
    def __init__(self, edicion_repo: EdicionRepositorio):
        """
        Inicializa el controlador con un repositorio de ediciones.
        
        Args:
            edicion_repo (EdicionRepositorio): Repositorio para operaciones de ediciones.
        """
        self.edicion_repo = edicion_repo

    def crear_edicion(self, edicion: Edicion):
        """
        Crea una nueva edición para un evento.
        
        Args:
            edicion (Edicion): Edición a ser creada.
        """
        self.edicion_repo.crear(edicion)

    def obtener_edicion(self, id: int) -> Edicion:
        """
        Obtiene una edición por su ID.
        
        Args:
            id (int): ID de la edición.
            
        Returns:
            Edicion: La edición encontrada.
        """
        return self.edicion_repo.obtener(id)

    def actualizar_edicion(self, edicion: Edicion):
        """
        Actualiza una edición existente.
        
        Args:
            edicion (Edicion): Edición con datos actualizados.
        """
        self.edicion_repo.actualizar(edicion)

    def eliminar_edicion(self, id: int):
        """
        Elimina una edición por su ID.
        
        Args:
            id (int): ID de la edición a eliminar.
        """
        self.edicion_repo.eliminar(id)
