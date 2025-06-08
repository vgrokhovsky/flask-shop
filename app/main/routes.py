from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.db.models import Product, User
from app.db import db_object as db
from . import main


@main.route("/")
def index():
    page = request.args.get("page", 1, type=int)
    per_page = 3
    pagination = Product.query.paginate(page=page, per_page=per_page, error_out=False)
    products = pagination.items
    return render_template("main/index.html", products=products, pagination=pagination)
