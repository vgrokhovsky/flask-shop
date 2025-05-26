from flask import render_template, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from db import models, db, User
from . import auth
from forms import RegistrationForm, LoginForm
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash


app = Flask(__name__)
app.config.from_object('config.Config')
db = SQLAlchemy(app)


login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'auth.login' 


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        flash("Account created for {}".format(form.username.data), category="success")
        return redirect(url_for("auth.login"))
    return render_template("register.html", form=form)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for("main.index"))
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

@login_manager.user_loader
def load_user(user_id):
    return User.quety.get(int(user_id))

@auth.route('/register',methods=['GET','POST'])
def register():
    form= RegistrationForm()
    if form.validate_on_submit():
        user= User(sername=form.username.data,email=form.email.data,password=form.password.data)
        db.session.add()
        db.session.commit()
        flash('Account created for {}'.format(form.usermane.data),category='success')
        return redirect(url_for('auth.login'))
    return render_template('register.html',form=form)

@auth.route('/logout')
@login_required
def logiut():
    logout_user
    return redirect(url_for('auth.login'))
