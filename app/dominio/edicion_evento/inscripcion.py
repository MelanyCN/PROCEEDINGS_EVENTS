class Inscripcion:
    """Representa una inscripción a un evento."""

    def __init__(self, id: int, evento_id: int, usuario_id: int, fecha):
        """
        Inicializa una instancia de Inscripcion.

        Args:
            id (int): El identificador único de la inscripción.
            evento_id (int): El identificador del evento asociado.
            usuario_id (int): El identificador del usuario inscrito.
            fecha (datetime.date): La fecha de la inscripción.
        """
        self.id = id
        self.evento_id = evento_id
        self.usuario_id = usuario_id
        self.fecha = fecha

    def to_dict(self):
        """
        Convierte la instancia de Inscripcion en un diccionario.

        Returns:
            dict: Representación de la inscripción como diccionario.
        """
        return {
            "id": self.id,
            "evento_id": self.evento_id,
            "usuario_id": self.usuario_id,
            "fecha": self.fecha.isoformat() if self.fecha else None
        }
