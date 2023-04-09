# TO DO
from flask import Blueprint, render_template, redirect, url_for, request
from models.auth import getUser

admin = Blueprint("admin", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

registered_admins = []

hrefs = ["/admin/admin"]
descriptions = ["Realizar admin"]

@admin.route('/')
def admin_index():
    return render_template('/admin/index.html', 
                           user=getUser(), 
                           hrefs=hrefs, 
                           descriptions=descriptions)