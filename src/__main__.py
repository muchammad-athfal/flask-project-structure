from flask import Flask

from src import routes

def main() -> Flask:
    
    app = Flask(__name__, template_folder="resources/views")
    
    routes.register(app)
    
    return app

def run():
    app = main()
    app.run(host="127.0.0.1", port=8000, debug=True)


if __name__ == "__main__":
    run()