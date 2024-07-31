
## Estilos de Programación

En este proyecto se han implementado varios estilos de programación para estructurar el código de manera efectiva y facilitar su mantenimiento y comprensión. A continuación, se describen los estilos utilizados y se proporcionan fragmentos de código representativos:

### 1. Cookbook
Se han utilizado funciones auxiliares para realizar operaciones comunes, encapsulando lógica reutilizable y simplificando el código principal.

**Fragmento de Código:**
```python
def parse_fecha(fecha_str):
    """Convierte una cadena de texto de fecha en un objeto datetime.date."""
    return datetime.strptime(fecha_str, "%Y-%m-%d").date() if fecha_str else None

def parse_autor(data):
    """Convierte un diccionario en un objeto Autor."""
    return Autor(**data) if data else None
```

### 2. Pipeline
Las rutas en la aplicación se configuran de manera secuencial, utilizando funciones que encadenan operaciones para manejar las solicitudes HTTP.

**Fragmento de Código:**
```python
def configurar_rutas_documentos(app):
    """Configura las rutas para documentos."""
    @app.route('/documento', methods=['POST'])
    def crear_documento():
        data = request.get_json()
        documento = Documento(
            titulo=data['titulo'],
            descripcion=data['descripcion'],
            fecha_publicacion=parse_fecha(data['fecha_publicacion']),
            autor=parse_autor(data['autor'])
        )
        documento_controller.crear_documento(documento)
        return jsonify(documento.to_dict()), 201
```

### 3. Error/Exception Handling
Se maneja de manera explícita la captura de errores para proporcionar respuestas claras en caso de fallos.

**Fragmento de Código:**
```python
@app.route('/evento/<int:id>', methods=['PUT'])
def actualizar_evento(id):
    data = request.get_json()
    try:
        evento = EventoModelo.query.get(id)
        if not evento:
            return jsonify({"error": EVENTO_NO_ENCONTRADO}), 404
        evento.nombre = data.get('nombre')
        evento.fecha = parse_fecha(data.get('fecha'))
        evento_controller.actualizar_evento(evento)
        return jsonify(evento.to_dict())
    except Exception as e:
        return jsonify({"error": str(e)}), 400
```

### 4. Restful
El diseño de la API sigue los principios REST, utilizando rutas y métodos HTTP estándar para operaciones CRUD.

**Fragmento de Código:**
```python
@app.route('/evento/<int:id>', methods=['DELETE'])
def eliminar_evento(id):
    """Elimina un evento por su ID."""
    if evento_controller.eliminar_evento(id):
        return jsonify({"mensaje": "Evento eliminado"}), 200
    return jsonify({"error": "Evento no encontrado"}), 404
```

---

# Principios SOLID Aplicados

### 1. Separación de Responsabilidades (SRP)

El **Principio de Responsabilidad Única** establece que una clase debe tener una sola responsabilidad o razón para cambiar. En el proyecto, inicialmente la clase `EdicionEventoControllerImpl` gestionaba tanto la lógica para eventos como para ediciones, lo que resultaba en una mezcla de responsabilidades.

Para mejorar la modularidad y el mantenimiento del código, se separaron estas responsabilidades en dos clases distintas: `EventoControllerImpl` y `EdicionControllerImpl`.

**Antes:**

```python
class EdicionEventoControllerImpl(EdicionEventoController):
    def __init__(self, evento_repo, edicion_repo):
        self.evento_repo = evento_repo
        self.edicion_repo = edicion_repo

    # Métodos para eventos
    def crear_evento(self, evento): ...
    def obtener_evento(self, id): ...
    def actualizar_evento(self, evento): ...
    def eliminar_evento(self, id): ...

    # Métodos para ediciones
    def crear_edicion(self, edicion): ...
    def obtener_edicion(self, id): ...
    def actualizar_edicion(self, edicion): ...
    def eliminar_edicion(self, id): ...
```

**Después:**

```python
# Controlador para Eventos
class EventoControllerImpl(EventoController):
    def __init__(self, evento_repo: EventoRepositorio):
        self.evento_repo = evento_repo

    def crear_evento(self, evento: Evento):
        self.evento_repo.crear(evento)

    def obtener_evento(self, id: int):
        return self.evento_repo.obtener(id)

    def actualizar_evento(self, evento: Evento):
        self.evento_repo.actualizar(evento)

    def eliminar_evento(self, id: int):
        self.evento_repo.eliminar(id)

# Controlador para Ediciones
class EdicionControllerImpl(EdicionController):
    def __init__(self, edicion_repo: EdicionRepositorio):
        self.edicion_repo = edicion_repo

    def crear_edicion(self, edicion: Edicion):
        self.edicion_repo.crear(edicion)

    def obtener_edicion(self, id: int):
        return self.edicion_repo.obtener(id)

    def actualizar_edicion(self, edicion: Edicion):
        self.edicion_repo.actualizar(edicion)

    def eliminar_edicion(self, id: int):
        self.edicion_repo.eliminar(id)
```

### 2. Uso de Interfaces (OCP & ISP)

Se ha aplicado el **Principio de Abierto/Cerrado (OCP)** y el **Principio de Segregación de Interfaces (ISP)** para definir interfaces separadas para cada tipo de controlador. Esto permite extender la funcionalidad de los controladores sin modificar el código existente, cumpliendo con OCP. Además, la segregación de interfaces asegura que las clases no estén obligadas a implementar métodos que no necesitan, cumpliendo con ISP.

**Interfaces:**

```python
from abc import ABC, abstractmethod

class EventoController(ABC):
    @abstractmethod
    def crear_evento(self, evento: Evento):
        pass

    @abstractmethod
    def obtener_evento(self, id: int) -> Evento:
        pass

    @abstractmethod
    def actualizar_evento(self, evento: Evento):
        pass

    @abstractmethod
    def eliminar_evento(self, id: int):
        pass

class EdicionController(ABC):
    @abstractmethod
    def crear_edicion(self, edicion: Edicion):
        pass

    @abstractmethod
    def obtener_edicion(self, id: int) -> Edicion:
        pass

    @abstractmethod
    def actualizar_edicion(self, edicion: Edicion):
        pass

    @abstractmethod
    def eliminar_edicion(self, id: int):
        pass
```

### 3. Inyección de Dependencias (DIP)

El **Principio de Inversión de Dependencias (DIP)** se ha implementado para desacoplar los controladores de las implementaciones concretas de los repositorios. Esto facilita la sustitución de implementaciones y mejora la modularidad y el mantenimiento del código.

**Antes:**

```python
evento_repo = EventoRepositorioImpl()
edicion_repo = EdicionRepositorioImpl()
controller = EdicionEventoControllerImpl(evento_repo, edicion_repo)
```

**Después:**

```python
evento_repo = EventoRepositorioImpl()
edicion_repo = EdicionRepositorioImpl()
evento_controller = EventoControllerImpl(evento_repo)
edicion_controller = EdicionControllerImpl(edicion_repo)
```


## Prácticas de Codificación Legible Aplicadas

### 1. Uso de Nombres Descriptivos

Se han usado nombres descriptivos para métodos y variables, lo que facilita la comprensión del código sin necesidad de una documentación extensa. Los nombres como `crear`, `obtener`, `actualizar`, `eliminar`, y `convocatoria_org` indican claramente la función de cada método o variable.

**Ejemplo:**

```python
def obtener(self, id: int):
    """Obtiene una convocatoria por su ID."""
    # ...
```

### 2. Comentarios Claros y Concisos

**Docstrings:** Se han añadido docstrings a cada método para explicar su propósito, los parámetros que acepta, y lo que devuelve. Esto ayuda a otros desarrolladores a entender rápidamente el propósito de cada función.

**Comentarios en el Código:** Además, se han añadido comentarios en lugares clave para explicar decisiones de diseño o manejo de errores. Estos comentarios son breves pero informativos, proporcionando contexto adicional cuando es necesario.

**Ejemplo:**

```python
def crear(self, convocatoria_org: ConvocatoriaOrgModelo):
    """Crea una nueva convocatoria en la base de datos.

    Args:
        convocatoria_org (ConvocatoriaOrgModelo): La convocatoria a ser agregada a la base de datos.
    """
    try:
        db.session.add(convocatoria_org)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise RuntimeError(f"Error al crear la convocatoria: {str(e)}")
```

### 3. Manejo de Errores

Se ha implementado un manejo de errores robusto utilizando bloques `try-except`. Esto permite capturar excepciones, revertir transacciones fallidas (rollback), y relanzar errores con mensajes descriptivos que facilitan el diagnóstico y la corrección de problemas.

**Ejemplo:**

```python
except Exception as e:
    db.session.rollback()
    raise RuntimeError(f"Error al crear la convocatoria: {str(e)}")
```
```