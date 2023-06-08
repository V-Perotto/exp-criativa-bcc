# TO DO
from flask import Blueprint, render_template, redirect, url_for, request
from models.auth import getUser, getDbBoard, registerSensor, registerBoard
from models.auth import showBoards, showSensors

iot = Blueprint("IoT", __name__, template_folder='./views/', static_folder='./static/', root_path="./")

@iot.route('/')
def index():
    return render_template('/iot/index.html', 
                           user=getUser(),
                           db_board=getDbBoard() 
                           )

@iot.route("/Dashboard")
def dashboard():
    return render_template("/iot/dashboard.html",
                           user=getUser(),
                           db_board=getDbBoard)

@iot.route('/SensorsList')
def list_sensors():
    return render_template('/iot/list/index_sensors.html',
                           user=getUser(), 
                           db_board=getDbBoard()
                           )

@iot.route('/BoardsList')
def list_boards():
    return render_template('/iot/list/index_boards.html',
                           user=getUser(), 
                           db_board=getDbBoard()
                           )
    
@iot.route("/AddBoard")
def add_board():
    return render_template('/iot/create/index_board.html', 
                           user=getUser())
    
@iot.route("/AddSensor")
def add_sensor():
    return render_template('/iot/create/index_sensor.html', 
                           user=getUser())

@iot.route('/add_board', methods=['POST', 'GET'])
def create_board():
    name = request.form.get("name", None)
    registerBoard(name)
    return redirect(url_for("IoT.create_board"))

@iot.route('/add_sensor', methods=['POST', 'GET'])
def create_sensor():
    name = request.form.get("name", None)
    board_id = request.form.get("board_id", None)
    registerSensor(name, board_id)
    return redirect(url_for("IoT.create_sensor"))