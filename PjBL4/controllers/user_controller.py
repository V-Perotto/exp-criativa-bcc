from flask import Blueprint, render_template,redirect,url_for

user = Blueprint("user", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@user.route("/")
def user_index():
    return render_template("/user/user_index.html")