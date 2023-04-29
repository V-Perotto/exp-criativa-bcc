from flask import Blueprint, render_template, redirect, url_for, request
from models import Sensor

iot = Blueprint("iot", __name__, template_folder = './views/', static_folder='./static/', root_path="./")

@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route("/register_sensor")
def iot_register_sensor():
    return render_template("/iot/register_sensor.html")

@iot.route("/view_sensors")
def iot_view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors=sensors)

@iot.route("/save_sensor", methods=['POST', 'GET'])
def save_sensor():
    name = request.form.get("name", None)
    model = request.form.get("model", None)
    brand = request.form.get("brand", None)
    voltage = request.form.get("voltage", None)
    description = request.form.get("description", None)
    is_active = True if request.form.get("is_active", None) == "on" else False
    measure = request.form.get("measure", None)
    
    Sensor.save_sensor_alt(name, model, brand, voltage, description, is_active, measure)

    return redirect(url_for("iot.iot_view_sensors"))

@iot.route("/register_actuator")
def iot_register_actuator():
    return render_template("/iot/register_actuator.html")