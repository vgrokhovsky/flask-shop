from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.db.models import Product, User
from app.db import db_object as db
from app.db.db_func import get_products_pagination
from . import main


@main.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 3
    pagination = get_products_pagination(page, per_page)
    products = pagination.items
    return render_template("main/index.html", products=products, pagination=pagination)


@main.route("/account")
@login_required
def dashboard():
    products = (
        current_user.products
    )  # Получаем продукты, связанные с текущим пользователем
    return render_template("account.html", products=products)
