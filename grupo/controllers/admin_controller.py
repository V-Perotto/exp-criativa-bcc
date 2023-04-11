# TO DO
from flask import Blueprint, render_template, redirect, url_for, request
from models.auth import getUser, registerUser, db_users

admin = Blueprint("admin", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

# tela index de admin?

@admin.route('/Users')
def users_index():
    return render_template('/admin/Users/index.html', 
                           user=getUser())

@admin.route("/Users/Register")
def register_users():
    return render_template('/admin/Users/register_user.html', 
                           user=getUser())

@admin.route("/Users/UsersList")
def user_list():
    return render_template("/admin/Users/list_of_users.html",
                           user=getUser(),
                           db_users=db_users)

@admin.route('/Users/create_user', methods=['POST', 'GET']) 
def create_user():
    
    user_name = request.form.get("user_name", None)
    user_surname = request.form.get("user_surname", None)
    user_email = request.form.get("user_email", None)
    user_password = request.form.get("user_password", None)
    user_is_admin = request.form.get("user_is_admin", None)
    
    registerUser(user_name, user_surname, user_email, user_password, user_is_admin)
    return redirect(url_for("admin.create_user"))
