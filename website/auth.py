from flask import Blueprint

# define this file is a blueprint
auth = Blueprint('auth', __name__)


# Login route
@auth.route('/login')
def login():
    return "<p>Login</p>"


# Logout route
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


# sign-up route
@auth.route('/sign-up')
def sign_up():
    return "<p>Sign-Up</p>"
