from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from . import cart
from app.db.models import Product, Cartitem


@cart.route("/cart")
@login_required
def cart_view():
    cart_items = Cartitem.query.filter_by(user_id=current_user.id).all()
    return render_template("cart.html", cart_items=cart_items)


@cart.route("/add_to_cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    quantity = int(request.form.get("quantity", 1))
    product=Product.query.get_or_404(product_id)

    product = Product.query.get_or_404(product_id)

    product_in_cart = Cartitem.query.filter_by(
        user_id=current_user.id, product_id=product.id
    ).first()
    if product_in_cart:
        product_in_cart.quantity += quantity
    else:
        new_cart_item = Cartitem(
            user_id=current_user.id, product_id=product.id, quantity=quantity
        )
        db.session.add(new_cart_item)
    db.session.commit()
    flash("Товар добавлен в корзину!")
    return redirect("new_cart_item") # !!


# Удаление товара из корзины
@cart.route("/remove_item/<int:item_id>", methods=["POST"])
@login_required
def remove_item(item_id):
    item = Cartitem.query.get_or_404(item_id)
    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for("cart.cart_view"))
