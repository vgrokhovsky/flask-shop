from flask import render_template, request
from flask_login import login_required, current_user

from . import users
from app.db.db_func import get_wishlist
from app.db.models import User


@users.route("/user/<int:user_id>")
@login_required
def users_view(user_id):
    user_data = User.query.get_or_404(user_id)
    return render_template("user.html", user_data=user_data)


@users.route("/user/wishlist/<int:user_id>")
@login_required
def user_wishlist(user_id):
    wishlist = get_wishlist(user_id)
    return render_template("user_wishlist.html", wishlist=wishlist)
