from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import login_manager, LoginManager

# Database creation
db = SQLAlchemy()
DB_NAME = "notesDatabase.db"


# f string where db is located
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'randomstring'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    # check on the server if the db has been created yet
    from .models import User, Note
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    # telling flask what user is being looked for
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app


# checks if data exists and if not it will create it
def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')


SQLALCHEMY_TRACK_MODIFICATIONS = False
