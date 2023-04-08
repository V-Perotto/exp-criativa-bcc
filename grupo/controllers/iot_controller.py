# TO DO
from flask import Blueprint, render_template, redirect, url_for, request

iot = Blueprint("IoT", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

registered_iots = []

hrefs = ["/IoT/register"]
descriptions = ["Registrar Sensor"]

@iot.route('/')
def index():
    return render_template('/iot/index.html', hrefs=hrefs, descriptions=descriptions)

@iot.route('/save_board', methods=['POST', 'GET'])
def save_register():
    global db_board

    board_sensor_name = request.form.get("board_sensor_name", None)
    board_sensor_status = request.form.get("board_sensor_status", None)
    
    dict_board = {
        "name": board_sensor_name,
        "status": board_sensor_status
    }

    db_board.append(dict_board)
    return redirect(url_for("board.register"))