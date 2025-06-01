from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.db.models import User, Product
from app.db import db_object as db


def init_admin(app):
    admin = Admin(app, name='My Admin', template_mode='bootstrap4')

    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Product, db.session))


