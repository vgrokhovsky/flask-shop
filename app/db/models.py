from flask_login import UserMixin

from . import db_object as db 

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, unique=True, nullable=False)
    cart_items = db.relationship("Cartitem", back_populates="user", lazy=True)

    products = db.relationship('Product', backref='user', lazy=True)

class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    stock = db.Column(db.String, nullable=False)
    image_path = db.Column(db.String, nullable=False)

    user = db.relationship('User', backref='products')
    cart_items = db.relationship("Cartitem", back_populates="product")


class Cartitem(db.Model):
    __tablename__ = "cartitem"
    
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)

    user = db.relationship('User', back_populates='cart_items')
    product = db.relationship('Product', back_populates='cart_items')