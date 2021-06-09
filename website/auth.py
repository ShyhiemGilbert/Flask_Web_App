from flask import Blueprint, render_template, request, flash

# define this file is a blueprint
auth = Blueprint('auth', __name__)


# Login route
@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", boolean="True")


# Logout route
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


# sign-up route
@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        lastName = request.form.get('lastName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
       # if length of email is less than 4, then
        if len(email) < 4:
            # flash a message is email is too short
            flash('Email must be greater than 4 characters.', category='error')

        # if length of first name is less than 2, then
        elif len(firstName) < 2:
            flash('First name must be greater than 1 characters.', category='error')

        # if length of last name is less than 2, then
        elif len(lastName) < 2:
            flash('Last name must be greater than 1 characters.', category='error')

        # if both passwords do not match, then
        elif password1 != password2:
            flash('Passwords do not match.', category='error')

        # if length of password is less than 7, then
        elif len(password1) < 7:
            flash('Password must be greater than 1 characters.', category='error')

        else:
            flash('Account successfully created!', category='success')

    return render_template("sign_up.html")
