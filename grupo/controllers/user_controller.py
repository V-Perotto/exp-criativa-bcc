from flask import Blueprint, render_template, redirect, url_for, request
from models.auth import getUser, registerUser, validate_login
from models.auth import db_users

user = Blueprint("user", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@user.route('/')
def user_index():
    return render_template('/user/index.html', 
                           user=getUser()
                           )

# register user
@user.route('/register')
def register():
    return render_template('/user/register.html', 
                           user=getUser(), 
                           db_users = db_users)

@user.route('/save_register', methods=['POST', 'GET'])
def save_register():
    user_name = request.form.get("user_name", None)
    user_surname = request.form.get("user_surname", None)
    user_email = request.form.get("user_email", None)
    user_password = request.form.get("user_password", None)
    # user_birthday = request.form.get("user_birthday", None)
    
    registerUser(user_name, user_surname, user_email, user_password)
    return redirect(url_for("user.register"))

# login
@user.route('/login', methods=['POST', 'GET'])
def user_login():
    global db_users 
    
    user_email = request.form.get("user_email", None)
    user_pwd = request.form.get("user_password", None)
    
    is_valid = validate_login(user_email, user_pwd)
    
    return render_template('/user/login.html', 
                           user=getUser(), 
                           user_registered = is_valid)