from flask import abort, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import orders
from app.db.db_func import (
    create_order,
    add_order_item,
    get_orders_by_user,
    get_order_by_id,
    get_order_items,
)


@orders.route("/create_order", methods=["POST"])
@login_required
def create_order_route():
    order = create_order(current_user.id, "new")
    flash("Заказ успешно создан!")
    return redirect(url_for("orders.order_details", order_id=order.id))


@orders.route("/add_order_item/<int:order_id>", methods=["POST"])
@login_required
def add_order_item_route(order_id):
    product_id = request.form.get("product_id")
    quantity = request.form.get("quantity")
    price = request.form.get("price")

    add_order_item(order_id, product_id, quantity, price)
    flash("Товар добавлен в заказ!")
    return redirect(url_for("orders.order_details", order_id=order_id))


@orders.route("/orders")
@login_required
def orders_view():
    orders = get_orders_by_user(current_user.id)
    return render_template("orders.html", orders=orders)


@orders.route("/order/<int:order_id>")
@login_required
def order_details(order_id):
    order = get_order_by_id(order_id)
    if order.user_id != current_user.id:
        abort(403)  # доступ запрещен
    # items = get_order_items(order_id)
    items = order.order_items
    return render_template("order_details.html", order=order, items=items)
