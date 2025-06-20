from flask import Flask

from app.db import db_object as db
from app.admin import init_admin
from app.auth.routes import login_manager


import os



def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = (
        f"mariadb+mariadbconnector://{os.getenv('MARIADB_USER')}:"
        f"{os.getenv('MARIADB_PASSWORD')}@{os.getenv('MARIADB_HOST')}:"
        f"{os.getenv('MARIADB_PORT')}/{os.getenv('MARIADB_DATABASE')}"
    )

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        db.create_all()

    init_admin(app)

    from .main import main as main_bp
    from .auth import auth as auth_bp
    from .products import products as products_bp
    from .cart import cart as cart_bp
    from .users import users as users_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(users_bp)

    return app
