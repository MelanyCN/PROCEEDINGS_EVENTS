from flask import Flask

app = Flask(__name__)

from app.presentacion import routes
