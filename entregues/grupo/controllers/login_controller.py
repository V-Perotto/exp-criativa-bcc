# TO DO
from flask import Blueprint, render_template, redirect, url_for, request
from models.auth import getUser

login = Blueprint("login", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@login.route('/')
def login_index():
    return render_template('/login/index.html', 
                           user=getUser()
                            
                          )