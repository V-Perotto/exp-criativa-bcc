from flask import Blueprint, render_template,redirect,url_for, request
from models import Sensor
iot = Blueprint("iot", __name__, template_folder = './views/admin/', static_folder='./static/', root_path="./")

@iot.route("/")
def iot_index():
    return render_template("/iot/iot_index.html")

@iot.route("/register_sensor")
def register_sensor():
    return render_template("/iot/register_sensor.html")

@iot.route("/view_sensors")
def view_sensors():
    sensors = Sensor.get_sensors()
    return render_template("/iot/view_sensors.html", sensors = sensors)

@iot.route("/save_sensors", methods = ["POST"])
def save_sensors():
    name = request.form.get("name")
    brand = request.form.get("brand")
    model = request.form.get("model")
    description = request.form.get("description")
    measure = request.form.get("measure")
    voltage = request.form.get("voltage")
    is_active = True if request.form.get("is_active") == "on" else False

    Sensor.save_sensor(name, brand, model, description ,voltage, is_active, measure)

    return redirect(url_for('admin.iot.view_sensors'))