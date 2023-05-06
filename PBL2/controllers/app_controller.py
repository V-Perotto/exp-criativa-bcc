from flask import Flask, render_template, session, g
from controllers.admin_controller import admin
from controllers.auth_controller import auth
from flask_login import LoginManager

from models.db import db, instance 

def create_app() -> Flask:
    app = Flask(__name__, template_folder="./views/", 
                        static_folder="./static/", 
                        root_path="./")
    
    app.config["TESTING"] = False
    app.config['SECRET_KEY'] = 'generated-secrete-key'
    app.config["SQLALCHEMY_DATABASE_URI"] = instance
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return User.query.get(int(user_id))

    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(admin, url_prefix='/admin')
    

    @app.route('/')
    def index():
        return render_template("home.html")
    
    return app