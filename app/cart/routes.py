from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from . import cart
from app.db.models import Product, Cartitem
from app.db.db_func_cart import (
    get_cart_items,
    update_cart_item_quantity,
    get_cart_total,
)
from app.db.db_func import get_product_by_id


@cart.route("/cart", methods=["GET"])
@login_required
def cart_view():
    cart_items = get_cart_items(current_user.id)
    total = get_cart_total(current_user.id)
    # total = 0
    # for cart_item in cart_items:
    #     total += cart_item.quantity * cart_item.product.price

    return render_template(
        "cart.html", cart_items=cart_items, products=cart_items, total=total
    )


@cart.route("/add_to_cart/<int:product_id>", methods=["POST"])
@login_required
def add_to_cart(product_id):
    quantity = int(request.form.get("quantity", 1))
    product = get_product_by_id(product_id)
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
    return redirect("new_cart_item")  # !!


# Удаление товара из корзины
@cart.route("/remove_item/<int:item_id>", methods=["POST"])
@login_required
def remove_item(item_id):
    item = Cartitem.query.get_or_404(item_id)
    if item.user_id == current_user.id:
        db.session.delete(item)
        db.session.commit()
    return redirect(url_for("cart.cart_view"))


# Обновление количества в корзине
@cart.route("/update_cart/<int:cart_item_id>", methods=["POST"])
@login_required
def update_cart(cart_item_id):
    new_quantity = int(request.form.get("quantity", 1))
    update_cart_item_quantity(cart_item_id, new_quantity)
    flash("Количество товара обновлено!")
    return redirect(url_for("cart.cart_view"))


# получения общей стоимости в корзине
@cart.route("/cart_total", methods=["GET"])
@login_required
def cart_total():
    total = get_cart_total(current_user.id)
    return render_template("cart_total.html", total=total)
