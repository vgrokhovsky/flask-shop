from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from db import models, Product, CartItem
from . import main
from ..forms import RegistrationForm, LoginForm, ProductForm


@main.route('/')
def index():
    products=Product.query.all()
    return render_template('index.html',products=products)


@main.route('/product/<int:product_id>')
def product(product_id):
    product=Product.query.get_or_404(product_id)
    return render_template('product.html',product=product)

@main.route('/cart')
def cart():
    cart_items=CartItem.queru.filter_by(user_id=current_user.id).all()
    return render_template("cart.html",cart_items=cart_items)

@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    pass