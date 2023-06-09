from models import *
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

def generate_seeds(db:SQLAlchemy):

    normal_user = User(email= "normal@alert.com", username = "normal", password=generate_password_hash("normal"), is_admin=False, created_at=datetime.now())
    admin_user = User(email="admin@alert.com", username = "admin", password=generate_password_hash("admin"), is_admin=True, created_at=datetime.now())
        
    db.session.add_all([normal_user, admin_user])
    db.session.commit()
    
    #IOT

    umidity_device = Device(brand = "ESP32", model = "ESP32", name = "Umidade", voltage = 5, description = "Sensor de umidade com medida em percentual")
    temperature_device = Device(brand = "ESP32", model = "ESP32", name = "Temperatura", voltage = 5, description = "Sensor de temperatura com unidade de medida em graus celsios")
    gas_device = Device(brand = "ESP32", model = "ESP32", name = "Gás", voltage = 5, description = "Sensor de gás de cozinha")
    db.session.add_all([umidity_device, temperature_device, gas_device])
    db.session.commit()

    umidity_sensor = Sensor(id = umidity_device.id, measure = "%")
    temperature_sensor = Sensor(id = temperature_device.id, measure = "ºC")
    gas_sensor = Sensor(id = gas_device.id, measure = "%")

    db.session.add_all([umidity_sensor, temperature_sensor, gas_sensor])
    db.session.commit()

    data = {}
    data["id"] = umidity_sensor.id
    data["brand"] = umidity_device.brand
    data["name"] = umidity_device.name
    data["model"] = "Teste Update"
    data["voltage"] = umidity_device.voltage
    data["description"] = umidity_device.description
    data["is_active"] = False
    data["measure"] = "Measure Teste"
    Sensor.update_sensor(data)

    
    
