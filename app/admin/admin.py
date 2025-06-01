from flask import Flask
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'  
app.config['SECRET_KEY'] = 'your_secret_key' 

admin = Admin(app, name='My Admin', template_mode='bootstrap3')


from db.models import User,Product

admin.add.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Product, db.session))



if __name__ == '__main__':
    app.run(debug=True)
