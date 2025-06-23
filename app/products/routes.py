from flask import render_template, request, abort

from . import products
from app.db.models import Product
from app.db.db_func import get_product_by_category_id, get_product_by_id


@products.route("/category/<int:category_id>")
def products_view(category_id):
    page = request.args.get("page", 1, type=int)
    per_page = 3

    # Получаем продукты этой категории
    products_query = get_product_by_category_id(category_id)
    pagination = products_query.paginate(page=page, per_page=per_page, error_out=False)
    products = pagination.items

    return render_template(
        "products/category.html",
        products=products,
        pagination=pagination,
        category_id=category_id,
    )


@products.route("/product/<int:product_id>")
def product(product_id):
    product = get_product_by_id(product_id)
    return render_template("product.html", product=product)
