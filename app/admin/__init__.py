from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.db.models import User, Product
from app.db import db_object as db
from app.admin.view import UserAdmin

def init_admin(app):
    admin = Admin(app, name='My Admin', template_mode='bootstrap4')

    admin.add_view(UserAdmin(User, db.session))
    admin.add_view(ModelView(Product, db.session))

# class Item(db.Model):
#     id=db.Colimn(db.integer,primary_key=True)
#     name=db.Column(db.Sting)

# @app.before_first_request
# def create_data():
#      db.session.add_all([Item(name=f'Item {i}') for i in range(1, 101)])
#      db.session.commit()


# @app.route('/items', methods=['GET'])
# def items():
#     page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
#     total = Item.query.count()
#     items = Item.query.limit(per_page).offset(offset).all()
#     pagination = Pagination(page=page, total=total, record_name='items', per_page=per_page)

#     return render_template('index.html', items=items, pagination=pagination)

