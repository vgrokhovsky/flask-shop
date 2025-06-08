from flask import render_template, request
from flask_login import login_required, current_user

from . import users
from app.db.models import User


@users.route("/user/<int:user_id>")
@login_required
def users_view(user_id):
    user_data = User.query.get_or_404(user_id)
    return render_template("user.html", user_data=user_data)
