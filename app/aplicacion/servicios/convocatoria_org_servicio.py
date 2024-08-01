from abc import ABC, abstractmethod
from app.dominio.evento.convocatoria_org import ConvocatoriaOrg, ConvocatoriaOrgRepositorio

class ConvocatoriaOrgServicio(ABC):
    @abstractmethod
    def crear_convocatoria_org(self, convocatoria_org: ConvocatoriaOrg):
        pass

    @abstractmethod
    def obtener_convocatoria_org(self, id: int) -> ConvocatoriaOrg:
        pass

    @abstractmethod
    def actualizar_convocatoria_org(self, convocatoria_org: ConvocatoriaOrg):
        pass

    @abstractmethod
    def eliminar_convocatoria_org(self, id: int):
        pass

class ConvocatoriaOrgServicioImpl(ConvocatoriaOrgServicio):
    def __init__(self, convocatoria_org_repo: ConvocatoriaOrgRepositorio):
        """
        Inicializa el servicio con un repositorio de convocatorias de organización.
        
        Args:
            convocatoria_org_repo (ConvocatoriaOrgRepositorio): Repositorio para operaciones de convocatoria.
        """
        self.convocatoria_org_repo = convocatoria_org_repo

    def crear_convocatoria_org(self, convocatoria_org: ConvocatoriaOrg):
        """
        Crea una nueva convocatoria de organización en el repositorio.
        
        Args:
            convocatoria_org (ConvocatoriaOrg): Convocatoria de organización a ser creada.
        """
        self.convocatoria_org_repo.crear(convocatoria_org)

    def obtener_convocatoria_org(self, id: int) -> ConvocatoriaOrg:
        """
        Obtiene una convocatoria de organización por su ID.
        
        Args:
            id (int): ID de la convocatoria de organización.
            
        Returns:
            ConvocatoriaOrg: La convocatoria encontrada.
        """
        return self.convocatoria_org_repo.obtener(id)

    def actualizar_convocatoria_org(self, convocatoria_org: ConvocatoriaOrg):
        """
        Actualiza una convocatoria de organización existente.
        
        Args:
            convocatoria_org (ConvocatoriaOrg): Convocatoria con datos actualizados.
        """
        self.convocatoria_org_repo.actualizar(convocatoria_org)

    def eliminar_convocatoria_org(self, id: int):
        """
        Elimina una convocatoria de organización por su ID.
        
        Args:
            id (int): ID de la convocatoria a eliminar.
        """
        self.convocatoria_org_repo.eliminar(id)