from flask import Flask
from config import Config
from app.infraestructura.extension import db
from app.presentacion.controller.routes import configure_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    configure_routes(app)

    return app