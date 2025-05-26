from .models import User
from . import db_object as db 


def create_user(username, email, password):
    user = User(
            username=username,
            email=email,
            password=password,
        )
    db.session.add(user)
    db.session.commit()

def get_user(email):
    return User.query.get_or_404(email)
