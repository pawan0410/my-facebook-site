from flask import Flask
from app.config import app_config
from app.extensions import db
from app.default.views import default_blueprint
from app.main.views import main_blueprint


def application(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    
    # Register extensions
    db.init_app(app)
    
    # Register Blueprints
    app.register_blueprint(default_blueprint)
    app.register_blueprint(main_blueprint)
    
    with app.app_context():
        db.create_all()
    return app
    
    