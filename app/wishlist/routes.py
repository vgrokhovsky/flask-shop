from flask import render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from . import wishlist
from app.db.db_func import add_to_wishlist,get_wishlist,remove_from_wishlist


@wishlist.route("/add_to_wishlist/<int:product_id>", methods=["POST"])
@login_required
def add_to_wishlist_route(product_id):
    add_to_wishlist(current_user.id, product_id)
    flash("Продукт добавлен в список желаемого!")
    return redirect(url_for("products_view"))


@wishlist.route("/wishlist", methods=["GET"])
@login_required
def wishlist_view():
    items = get_wishlist(current_user.id)
    return render_template("wishlist.html", wishlist_items=items)

@wishlist.route("/remove_from_wishlist/<int:item_id>", methods=["POST"])
@login_required
def remove_from_wishlist_route(item_id):
    remove_from_wishlist(item_id)
    flash("Продукт удален из списка желаемого!")
    return redirect(url_for("wishlist.wishlist_view"))