from app.dominio.documento.autor_repositorio import AutorRepositorio
from app.infraestructura.modelo.autor_modelo import AutorModelo
from app.infraestructura.extension import db

class AutorRepositorioImpl(AutorRepositorio):
    def __init__(self):
        # This method is intentionally left empty.
        pass

    def crear(self, autor):
        autor_modelo = AutorModelo.from_domain(autor)
        db.session.add(autor_modelo)
        db.session.commit()

    def obtener(self, id):
        autor_modelo = AutorModelo.query.get(id)
        return autor_modelo.to_domain() if autor_modelo else None

    def actualizar(self, autor):
        autor_modelo = AutorModelo.query.get(autor.id)
        if autor_modelo:
            autor_modelo.nombre = autor.nombre
            autor_modelo.email = autor.email
            db.session.commit()

    def eliminar(self, id):
        autor_modelo = AutorModelo.query.get(id)
        if autor_modelo:
            db.session.delete(autor_modelo)
            db.session.commit()