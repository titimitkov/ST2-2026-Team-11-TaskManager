from flask import Flask

from config.config import Config
from extensions import db
from models.task import Task
from views.home import home_bp
from controllers.task_controller import task_bp
from controllers.ai_controller import ai_bp

def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    app.register_blueprint(home_bp)
    
    app.register_blueprint(task_bp)
    
    app.register_blueprint(ai_bp)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)