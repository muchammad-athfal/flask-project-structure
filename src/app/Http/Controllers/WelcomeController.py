from flask import render_template
from src.app.Http.Controllers.Controller import Controller

class WelcomeController(Controller):
    def index():
        return render_template("welcome.html")