class Inscripcion:
    def __init__(self, id, evento_id, usuario_id, fecha):
        self.id = id
        self.evento_id = evento_id
        self.usuario_id = usuario_id
        self.fecha = fecha

    def to_dict(self):
        return {
            "id": self.id,
            "evento_id": self.evento_id,
            "usuario_id": self.usuario_id,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }