from edicion_evento_controller import EdicionEventoController

class EdicionEventoControllerImpl(EdicionEventoController):
    def __init__(self, evento_repo, edicion_repo):
        self.evento_repo = evento_repo
        self.edicion_repo = edicion_repo

    def crear_evento(self, evento):
        return self.evento_repo.crear(evento)

    def obtener_evento(self, id):
        return self.evento_repo.obtener(id)

    def actualizar_evento(self, evento):
        return self.evento_repo.actualizar(evento)

    def eliminar_evento(self, id):
        return self.evento_repo.eliminar(id)

    def crear_edicion(self, edicion):
        return self.edicion_repo.crear(edicion)

    def obtener_edicion(self, id):
        return self.edicion_repo.obtener(id)

    def actualizar_edicion(self, edicion):
        return self.edicion_repo.actualizar(edicion)

    def eliminar_edicion(self, id):
        return self.edicion_repo.eliminar(id)