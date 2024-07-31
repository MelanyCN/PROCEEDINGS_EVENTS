# Proyecto de Página Web de Proceedings de Eventos

Este proyecto es una aplicación web desarrollada en Flask y MongoEngine para gestionar los proceedings de eventos.

## Requisitos Previos

- Python 3.6 o superior
- pip (gestor de paquetes de Python)

## Creación y Activación de un Entorno Virtual

### En Windows

1. Abre una terminal (cmd, PowerShell, o Git Bash).
2. Navega al directorio del proyecto.
3. Crea un entorno virtual con el siguiente comando:

    ```bash
    python -m venv .venv
    ```

4. Activa el entorno virtual:

    ```bash
    .\.venv\Scripts\activate
    ```

### En Linux/MacOS

1. Abre una terminal.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual con el siguiente comando:

    ```bash
    python3 -m venv .venv
    ```

4. Activa el entorno virtual:

    ```bash
    . .venv/bin/activate
    ```

## Instalación de Requerimientos

Una vez que el entorno virtual esté activado, instala los paquetes necesarios usando el archivo `requirements.txt`.

1. Asegúrate de estar en el directorio del proyecto y que el entorno virtual esté activado.
2. Ejecuta el siguiente comando:

    ```bash
    pip install -r requirements.txt
    ```

Esto instalará Flask, MongoEngine y todas las demás dependencias necesarias para el proyecto.

# Implementaciones

Este repositorio contiene la implementación de un sistema para la gestión de eventos y sus correspondientes entidades como documentos, autores, ediciones, inscripciones, expositores, y programas. La aplicación sigue los principios de la arquitectura limpia, utilizando Flask como framework web y SQLAlchemy con SQLite para la gestión de datos. A continuación, se describen las prácticas de codificación legible empleadas en este proyecto, junto con fragmentos de código ilustrativos.

## Practicas de codificacion legible

### Uso de Nombres descripctivos

**Practica:** Asignar nombres claros y descriptivos a variables, funciones y clases para facilitar la comprensión del código. Esto incluye usar nombres que reflejen claramente la función o propósito del elemento de código.

**Fragmento de codigo**

```python
class DocumentoRepositorioImpl(DocumentoRepositorio):
    def crear(self, documento):
        documento_modelo = DocumentoModelo.from_domain(documento)
        db.session.add(documento_modelo)
        db.session.commit()

```

### Separacion de Responsabilidades

**Practica:** Mantener la lógica separada en diferentes capas de la aplicación, como controladores, repositorios y modelos. Esto mejora la organización del código y facilita el mantenimiento.

**Fragmento de Codigo**

```python
class DocumentoRepositorioImpl(DocumentoRepositorio):
    def crear(self, documento):
        documento_modelo = DocumentoModelo.from_domain(documento)
        db.session.add(documento_modelo)
        db.session.commit()
```

### Conversion entre Dominios y Modelos de Base de datos

**Practica:** Implementar métodos para convertir entre objetos de dominio y modelos de base de datos. Esto permite una separación clara entre la lógica de negocio y la lógica de persistencia.

**Fragmento de Codigo**

```python
@staticmethod
def from_domain(documento_dominio: DocumentoDominio):
    return DocumentoModelo(
        id=documento_dominio.id,
        titulo=documento_dominio.titulo,
        descripcion=documento_dominio.descripcion,
        fecha_publicacion=documento_dominio.fecha_publicacion,
        autor_id=documento_dominio.autor.id
    )

def to_domain(self):
    return DocumentoDominio(
        id=self.id,
        titulo=self.titulo,
        descripcion=self.descripcion,
        fecha_publicacion=self.fecha_publicacion,
        autor=None
    )
```

### Uso de Metodos Estaticos para Conversiones

**Practica:** Implementar métodos estáticos en los modelos de base de datos para convertir objetos de dominio a modelos de base de datos y viceversa. Esto centraliza la lógica de conversión y evita duplicación de código.

**Fragmento de Codigo**

```python
@staticmethod
def from_domain(documento_dominio: DocumentoDominio):
    return DocumentoModelo(
        id=documento_dominio.id,
        titulo=documento_dominio.titulo,
        descripcion=documento_dominio.descripcion,
        fecha_publicacion=documento_dominio.fecha_publicacion,
        autor_id=documento_dominio.autor.id
    )
```

## Principios SOLID aplicados

### Principio de Responsabilidad unica

**Practica:** Una clase debe tener una única responsabilidad o razón para cambiar. Este principio se asegura de que cada clase se enfoque en una tarea específica, lo que facilita el mantenimiento y la comprensión del código.

**Fragmento de Codigo** 

```python
class DocumentoRepositorioImpl(DocumentoRepositorio):
    def crear(self, documento):
        documento_modelo = DocumentoModelo.from_domain(documento)
        db.session.add(documento_modelo)
        db.session.commit()

    def obtener(self, id):
        documento_modelo = DocumentoModelo.query.get(id)
        return documento_modelo.to_domain() if documento_modelo else None
```

### Principio Abierto/Cerrado

**Practica:** El código debe estar abierto para extensión, pero cerrado para modificación. Esto significa que el comportamiento de una clase debe poder extenderse sin modificar su código fuente, facilitando la adición de nuevas funcionalidades sin afectar el código existente.

```python
@staticmethod
def from_domain(documento_dominio: DocumentoDominio):
    return DocumentoModelo(
        id=documento_dominio.id,
        titulo=documento_dominio.titulo,
        descripcion=documento_dominio.descripcion,
        fecha_publicacion=documento_dominio.fecha_publicacion,
        autor_id=documento_dominio.autor.id
    )

def to_domain(self):
    return DocumentoDominio(
        id=self.id,
        titulo=self.titulo,
        descripcion=self.descripcion,
        fecha_publicacion=self.fecha_publicacion,
        autor=None
    )
```

### Principio de Sustitucion de Liskov

**Practica:** Las clases derivadas deben ser sustituibles por sus clases base sin alterar el comportamiento esperado del programa. En otras palabras, un objeto de una clase derivada debe poder reemplazar un objeto de la clase base sin que el programa falle o se comporte incorrectamente.

**Fragmento de Codigo**

```python
class DocumentoRepositorioImpl(DocumentoRepositorio):
    def __init__(self):
        # This method is intentionally left empty.
        pass

    def crear(self, documento):
        documento_modelo = DocumentoModelo.from_domain(documento)
        db.session.add(documento_modelo)
        db.session.commit()

    def obtener(self, id):
        documento_modelo = DocumentoModelo.query.get(id)
        return documento_modelo.to_domain() if documento_modelo else None
```