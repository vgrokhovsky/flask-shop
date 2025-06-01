from flask_login import current_user
from flask_admin.contrib.sqla import ModelView
from admin import admin
from db.models import User,Product


class SecuredModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin  

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login', next=request.url))  

admin.add_view(SecuredModelView(User, db.session))
admin.add_view(SecuredModelView(Product, db.session))