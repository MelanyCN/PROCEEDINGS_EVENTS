class Edicion:
    def __init__(self, id, evento_id, nombre, fecha):
        self.id = id
        self.evento_id = evento_id
        self.nombre = nombre
        self.fecha = fecha

    def to_dict(self):
        return {
            "id": self.id,
            "evento_id": self.evento_id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }
