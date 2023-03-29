# TO DO
from flask import Blueprint, render_template, redirect, url_for, request

user = Blueprint("user", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

registered_users = []

hrefs = ["/user/user"]
descriptions = ["Realizar user"]

@user.route('/')
def user_index():
    return render_template('/user/index.html', hrefs=hrefs, descriptions=descriptions)