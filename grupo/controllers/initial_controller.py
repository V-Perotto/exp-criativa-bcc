# TO DO
from flask import Blueprint, render_template, redirect, url_for, request

initial = Blueprint("initial", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

registered_initials = []

hrefs = ["/initial/initial"]
descriptions = ["Realizar initial"]

@initial.route('/')
def initial_index():
    return render_template('/initial/index.html', hrefs=hrefs, descriptions=descriptions)