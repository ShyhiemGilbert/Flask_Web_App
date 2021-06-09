from flask import Blueprint, render_template

# define this file is a blueprint
auth = Blueprint('auth', __name__)


# Login route
@auth.route('/login')
def login():
    return render_template("login.html", boolean="True")


# Logout route
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


# sign-up route
@auth.route('/sign-up')
def sign_up():
    return render_template("sign_up.html")
