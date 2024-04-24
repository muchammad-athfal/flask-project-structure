from flask import Flask

from .web import web_blueprint
from .api import api_blueprint

def register(app: Flask) -> None:
    app.register_blueprint(web_blueprint)
    app.register_blueprint(api_blueprint)