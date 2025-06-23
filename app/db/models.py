from flask_login import UserMixin
from . import db_object as db


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)
    cart_items = db.relationship("Cartitem", back_populates="user", lazy=True)
    products = db.relationship("Product", backref="user", lazy=True)
    orders = db.relationship("Order", back_populates="user", lazy=True)
    products = db.relationship("Product", backref="user", lazy=True)


class Product(db.Model):
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.Text, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    image_path = db.Column(db.String(255), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    cart_items = db.relationship("Cartitem", back_populates="product")


class Cartitem(db.Model):
    __tablename__ = "cartitem"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)

    user = db.relationship("User", back_populates="cart_items")
    product = db.relationship("Product", back_populates="cart_items")


class Category(db.Model):
    __tablename__='category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    products = db.relationship("Product", backref="category", lazy=True)

 
class Order(db.Model):
    __tablename__ = "order"


    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    order_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    status = db.Column(db.String(100), nullable=False)

    user = db.relationship("User", back_populates="orders")
    order_items = db.relationship("OrderItem", back_populates="order")

class OrderItem(db.Model):
    __tablename__ = "order_item"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    order = db.relationship("Order", back_populates="order_items")
    product = db.relationship("Product")   

class Wishlist(db.Model):
    __tablename__ = "wishlist"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("product.id"), nullable=False)

    user = db.relationship("User", back_populates="wishlists")
    product = db.relationship("Product")

User.wishlists = db.relationship("Wishlist", back_populates="user")