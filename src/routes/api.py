from flask import Blueprint, g

api_blueprint = Blueprint("api", __name__, url_prefix="/api")

@api_blueprint.route("/")
def index():
    return "Hello, World!"