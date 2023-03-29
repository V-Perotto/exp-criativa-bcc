# TO DO
from flask import Blueprint, render_template, redirect, url_for, request

login = Blueprint("login", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

registered_logins = []

hrefs = ["/login/login"]
descriptions = ["Realizar Login"]

@login.route('/')
def login_index():
    return render_template('/login/index.html', hrefs=hrefs, descriptions=descriptions)