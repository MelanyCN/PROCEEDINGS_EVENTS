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