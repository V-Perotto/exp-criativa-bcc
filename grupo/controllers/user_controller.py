from flask import Blueprint, render_template, redirect, url_for, request
from models.auth import getUser

user = Blueprint("user", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

db_users = []

hrefs = ["/user/register", "/user/login"]
descriptions = ["Criar um Cadastro", "Realizar Login"]

@user.route('/')
def user_index():
    return render_template('/user/index.html', 
                           user=getUser(), 
                           hrefs=hrefs, 
                           descriptions=descriptions)

# register user
@user.route('/register')
def register():
    global db_users
    return render_template('/user/register.html', 
                           user=getUser(), 
                           hrefs=hrefs, 
                           descriptions=descriptions, 
                           register_list = db_users)

@user.route('/save_register', methods=['POST', 'GET'])
def save_register():
    global db_users

    user_name = request.form.get("user_name", None)
    user_surname = request.form.get("user_surname", None)
    user_email = request.form.get("user_email", None)
    user_pwd = request.form.get("user_pwd", None)
    # user_birthday = request.form.get("user_birthday", None)
    
    dict_user = {
        "user_name": user_name,
        "user_surname": user_surname,
        "user_email": user_email,
        "user_pwd": user_pwd
    }
    db_users.append(dict_user)
    return redirect(url_for("user.register"))

# login
@user.route('/login', methods=['POST', 'GET'])
def user_login():
    global db_users 
    
    user_email = request.form.get("user_email", None)
    user_pwd = request.form.get("user_pwd", None)
    
    is_valid = validate_login(user_email, user_pwd)
    
    return render_template('/user/login.html', 
                           user=getUser(), 
                           hrefs=hrefs, 
                           descriptions=descriptions, 
                           user_registered = is_valid)

def validate_login(user_email, user_pwd):
    global db_users
    for user in db_users:
        if user['user_email'] == user_email and user["user_pwd"] == user_pwd:
            return True
    return False 
# @user.route('/save_login', methods=['POST', 'GET'])
# def save_login():
#     global db_users 

#     user_email = request.form.get("user_email", None)
#     user_pwd = request.form.get("user_pwd", None)
#     return render_template('/user/login.html', hrefs=hrefs, descriptions=descriptions, registered_users = db_users)