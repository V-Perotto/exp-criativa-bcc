# TO DO
from flask import Blueprint, render_template, redirect, url_for, request

iot = Blueprint("iot", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

registered_iots = []

hrefs = ["/iot/iot"]
descriptions = ["Realizar iot"]

@iot.route('/')
def iot_index():
    return render_template('/iot/index.html', hrefs=hrefs, descriptions=descriptions)