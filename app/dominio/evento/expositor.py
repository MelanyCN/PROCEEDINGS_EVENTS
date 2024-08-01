class Expositor:
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "email": self.email,
        }