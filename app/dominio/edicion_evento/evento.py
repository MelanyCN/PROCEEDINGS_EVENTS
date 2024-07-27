class Evento:
    def __init__(self, id, nombre, fecha):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }