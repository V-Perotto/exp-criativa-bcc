from flask import Blueprint, render_template, redirect, url_for, request
from models import Sensor, Actuator, Convenient

iot = Blueprint("iot", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")


@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route("/register_sensor")
def register_sensor():
    return render_template("/iot/register_sensor.html")

@iot.route("/view_sensors")
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors=sensors)

@iot.route("/save_sensors", methods=["POST"])
def save_sensors():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    convenient = request.form.get("convenient")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, description,
                       convenient, is_active, measure)

    return redirect(url_for('admin.iot.view_sensors'))


@iot.route("/register_actuator")
def iot_register_actuator():
    return render_template("/iot/register_actuator.html")

@iot.route("/view_actuators")
def iot_view_actuators():
    actuators = Actuator.get_actuators()
    return render_template("/iot/view_actuators.html", actuators=actuators)

@iot.route("/save_actuator", methods=["POST", "GET"])
def save_actuator():
    name = request.form.get("name", None)
    model = request.form.get("model", None)
    brand = request.form.get("brand", None)
    convenient = request.form.get("convenient", None)
    description = request.form.get("description", None)
    is_active = True if request.form.get("is_active", None) == "on" else False
    type = request.form.get("type", None)

    Actuator.save_actuator_2(name, model, brand, convenient,
                             description, is_active, type)

    return redirect(url_for("admin.iot.iot_view_actuators"))

@iot.route("/view_convenient")
def iot_view_convenient():
    convenients = Sensor.get_convenient()
    return render_template("/iot/view_convenient.html", convenients=convenients)
