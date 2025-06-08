from flask_admin.contrib.sqla import ModelView

from app.db.models import User, Product


class UserAdmin(ModelView):
    column_list = ("username", "email", "password")
