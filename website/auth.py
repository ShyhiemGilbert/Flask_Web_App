from flask import Blueprint, render_template, request, flash, url_for
from werkzeug.utils import redirect
from . import db
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user

# define this file is a blueprint
auth = Blueprint('auth', __name__)


# Login route
# sees if the user is logged in
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist, please try again.', category='error')

    return render_template("login.html", user=current_user)


# Logout route
@auth.route('/logout')
# cannot access this if not logged in
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


# sign-up route
@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        # making sure users are not applying with the same email
        user = User.query.filter_by(email=email).first()
        if user:
            flash('This email already exists.', category='error')
        # if length of email is less than 4, then
        if len(email) < 4:
            # flash a message is email is too short
            flash('Email must be greater than 4 characters.', category='error')

        # if length of first name is less than 2, then
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.', category='error')

        # if length of last name is less than 2, then
        elif len(last_name) < 2:
            flash('Last name must be greater than 1 characters.', category='error')

        # if both passwords do not match, then
        elif password1 != password2:
            flash('Passwords do not match.', category='error')

        # if length of password is less than 7, then
        elif len(password1) < 7:
            flash('Password must be greater than 1 characters.', category='error')

        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            # log in new user
            flash('logged in successfully!', category='success')
            flash('Account successfully created!', category='success')

            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)
