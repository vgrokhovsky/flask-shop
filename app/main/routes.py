from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.db.models import Product, Cartitem, User
from . import main


@main.route('/')
def index():
    products=Product.query.all()
    return render_template('main/index.html', products=products)
    # return render_template('index.html',products=[])


@main.route('/product/<int:product_id>')
def product(product_id):
    product=Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@main.route('/cart')
def cart():
    cart_items=Cartitem.queru.filter_by(user_id=current_user.id).all()
    return render_template("cart.html", cart_items=cart_items)

@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    pass

