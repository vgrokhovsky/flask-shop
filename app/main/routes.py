from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.db.models import Product, Cartitem, User
from app.db import db_object as db
from . import main


# @main.route('/')
# def index():
#     products=Product.query.all()
#     return render_template('main/index.html', products=products)
#     # return render_template('index.html',products=[])

# def pagination_func(model, request):
#     page = request.args.get('page', 1, type=int)
#     per_page = 10
#     pagination = model.query.paginate(page=page, per_page=per_page, error_out=False)
#     model_items = pagination.items
#     return model_items, pagination


@main.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    per_page = 3
    pagination = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    products = pagination.items
    return render_template('main/index.html', products=products, pagination=pagination)

@main.route('/product/<int:product_id>')
def product(product_id):
    product=Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)

@main.route('/cart')
@login_required
def cart():
    cart_items=Cartitem.queru.filter_by(user_id=current_user.id).all()
    return render_template("cart.html", cart_items=cart_items)

@main.route('/add_to_cart/<int:product_id>', methods=['POST'])
@login_required
def add_to_cart(product_id):
    quantity = int(request.form.get('quantity'))

    product = Product.query.get_or_404(product_id)

    product_in_cart = Cartitem.query.filter_by(
        user_id=current_user.id,
        product_id=product.id)
    if product_in_cart:
        product_in_cart.quantity += 1
    else:
        new_cart_item = Cartitem(user_id=current_user.id, product_id=product.id, quantity=quantity)
        db.session.add(new_cart_item)
    db.session.commit()
    return redirect('main.cart')