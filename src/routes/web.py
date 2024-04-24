from flask import Blueprint, g

from src.app.Http.Controllers.WelcomeController import WelcomeController

web_blueprint = Blueprint("web", __name__)

@web_blueprint.route("/")
def index():
    return WelcomeController.index()