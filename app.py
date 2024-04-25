from flask import Flask

from src import routes

def main() -> Flask:
    app = Flask(__name__, template_folder="src/resources/views")
    
    routes.register(app)
    
    return app


app = main()

if __name__ == "__main__":
    app.run()
