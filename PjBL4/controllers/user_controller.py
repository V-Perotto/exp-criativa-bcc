from flask import Blueprint, render_template, redirect, url_for, request
from models import User

user = Blueprint("user", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@user.route("/")
def user_index():
    return render_template("admin/admin_index.html")

@user.route("/register_user")
def register_user():
    return render_template("/user/register_user.html")

@user.route("/view_user")
def view_users():
    users = User.get_user()
    return render_template("/user/view_user.html", users=users)

@user.route("/save_user", methods=['POST', 'GET'])
def create_user():
    email = request.form.get("input_email")
    username = request.form.get("input_username")
    password = request.form.get("input_pwd")
    is_admin = True if request.form.get("checkbox_is_admin") == "on" else False
    
    try:
        User.save_user(email, username, password, is_admin)
    except Exception as e:
        pass

    return redirect(url_for('admin.user.view_users'))

@user.route("/delete_user/<int:user_id>", methods=['POST', 'GET'])
def remove_user(user_id):
    User.delete_user(user_id)
    return redirect(url_for('admin.user.view_users'))