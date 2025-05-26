from flask import Flask
from app.db import db_object as db
from app.db import models
from app.auth.routes import login_manager
from config import SQLALCHEMY_DATABASE_URI


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'key'

    db.init_app(app)
    login_manager.init_app(app)
    
    with app.app_context():
        db.create_all()

    from .main import main as main_bp
    from .auth import auth as auth_bp
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)

    return app
