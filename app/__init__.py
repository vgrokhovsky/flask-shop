from flask import Flask
from app.db import db_object as db
from app.db import models
from config import SQLALCHEMY_DATABASE_URI


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        db.create_all()

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    return app
