from flask import Blueprint, render_template
from flask_login import login_required, current_user

# define this file is a blueprint
views = Blueprint('views', __name__)

@views.route('/')
# cannot get to homepage if not logged  in
@login_required
def home():
    return render_template("home.html", user=current_user )