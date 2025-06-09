from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from app.db.db_func import create_user, get_user
from .forms import RegistrationForm, LoginForm
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash

from app.db.models import User

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        create_user(username, email, password)
        flash("Account created for {}".format(form.username.data), category="success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print('validate_on_submit')
        print('form.email.data', form.email.data)
        user = get_user(email=form.email.data)
        print(user.password, form.password.data)
        # if check_password_hash(user.password, form.password.data):
        if user.password == form.password.data:
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect('next_page')
            else:
                return redirect('index')
        else:
            flash(
                "Login Unsuccessful. Please check email and password", category="danger"
            )
    return render_template("login.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


# @app.route('/profile')
# @login_required
# def profile():
#     return render_template('profile.html', name=current_user.username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)