# TO DO
from flask import Blueprint, render_template, redirect, url_for, request
from models.auth import getUser, showBoards, showSensors

iot = Blueprint("IoT", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@iot.route('/')
def index():
    return render_template('/iot/index.html', 
                           user=getUser(), 
                           )
@iot.route('/SensorsList')
def list_sensors():
    return render_template('iot/list/index_sensors.html',
                           user=getUser(), 
                           db_board=showSensors()
                           )

@iot.route('/BoardsList')
def list_boards():
    return render_template('iot/list/index_boards.html',
                           user=getUser(), 
                           db_board=showBoards()
                           )

@iot.route('/add_board', methods=['POST', 'GET'])
def add_board():
    global db_board

    name = request.form.get("name", None)
    status = request.form.get("status", None)
    
    dict_board = {
        "name": name,
        "status": status
    }

    db_board.append(dict_board)
    return redirect(url_for("board.add_board"))

@iot.route('/add_sensor', methods=['POST', 'GET'])
def add_sensor():
    global db_board

    name = request.form.get("name", None)
    status = request.form.get("status", None)
    
    dict_board = {
        "name": name,
        "status": status
    }

    db_board.append(dict_board)
    return redirect(url_for("board.add_sensor"))