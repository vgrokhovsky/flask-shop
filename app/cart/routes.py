from flask import render_template, request
from flask_login import login_required, current_user

from . import cart
from app.db.models import Product, Cartitem


@cart.route("/")
@login_required
def cart_view():
    cart_items = Cartitem.queru.filter_by(user_id=current_user.id).all()
    return render_template("cart.html", cart_items=cart_items)


@cart.route("/add_to_cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    quantity = int(request.form.get("quantity"))

    product = Product.query.get_or_404(product_id)

    product_in_cart = Cartitem.query.filter_by(
        user_id=current_user.id, product_id=product.id
    )
    if product_in_cart:
        product_in_cart.quantity += 1
    else:
        new_cart_item = Cartitem(
            user_id=current_user.id, product_id=product.id, quantity=quantity
        )
        db.session.add(new_cart_item)
    db.session.commit()
    return redirect("main.cart")
