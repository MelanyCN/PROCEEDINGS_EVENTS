class Evento:
    def __init__(self, id=None, nombre=None, fecha=None, descripcion=None, hora=None, lugar=None):
        self.id = id
        self.nombre = nombre
        self.fecha = fecha
        self.descripcion = descripcion
        self.hora = hora
        self.lugar = lugar

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "fecha": self.fecha.isoformat() if self.fecha else None,
            "descripcion": self.descripcion,
            "hora": self.hora.isoformat() if self.hora else None,
            "lugar": self.lugar
        }