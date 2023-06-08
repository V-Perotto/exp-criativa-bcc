from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user
from models import User

auth = Blueprint("auth", __name__, 
                    template_folder="./views/", 
                    static_folder='./static/', 
                    root_path="./")

@auth.route("/")
@auth.route("/login")
def login():
    return render_template("auth/login.html")

@auth.route('/logout')
def logout():
    return redirect(url_for('index'))

@auth.route('/login_post', methods=['POST'])
def login_post():
    # login code goes here
    login_info = request.form.get('login')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    return redirect(url_for('admin.admin_index'))

@auth.route('/signup')
def signup():
    return render_template("auth/signup.html")

@auth.route('/signup_post', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    username = request.form.get("username", None)
    email = request.form.get("email", None)
    password = request.form.get("password", None)
    

    return redirect(url_for('auth.login'))