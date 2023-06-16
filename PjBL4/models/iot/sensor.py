from models import db, Device

class Sensor(db.Model):
    __tablename__ = "sensors"
    id = db.Column("id", db.Integer, db.ForeignKey(Device.id), primary_key = True)
    measure = db.Column(db.String(20))

    reads = db.relationship("Read", backref="sensors", lazy=True)

    def get_sensors():
        sensors = Sensor.query.join(Device, Device.id == Sensor.id)\
                    .add_columns(Sensor.id, Device.name, Device.brand, Device.model, 
                                 Device.convenient, Device.description,  Device.is_active, Sensor.measure).all()
        
        return sensors
    
    def get_convenient():
        sensors = Sensor.query.join(Device, Device.id == Sensor.id)\
                    .add_columns(Sensor.id, Device.name, Device.brand, Device.model, 
                                 Device.convenient, Device.description,  Device.is_active, Sensor.measure).all()
        return sensors
    
    def save_sensor(name, brand, model, description, convenient, is_active, measure):
        device = Device(name = name, brand = brand, model = model, 
                            description = description, convenient = convenient, is_active = is_active)
    
        sensor = Sensor(id = device.id, measure = measure)
        
        device.sensors.append(sensor)
        db.session.add(device)
        db.session.commit()

    def delete_sensor(id):
        sensor = Sensor.query.filter(Sensor.id == id).first()
        Sensor.query.filter_by(measure="%").delete()
        sensor.delete()

    def delete_sensor_by_measure(measure):
        Sensor.query.filter_by(measure=measure).delete()
        db.session.commit()

    def update_sensor(data):
        Device.query.filter_by(id=data['id'])\
                .update(dict(name = data['name'], brand=data['brand'], model = data['model'], 
                        voltage = data['voltage'], description = data['description'], 
                        is_active = data['is_active']))
        
        Sensor.query.filter_by(id=data['id'])\
                        .update(dict(measure = data['measure']))
        db.session.commit()

    def update_sensor_power(data):
        Device.query.filter_by(id=data['id'])\
                .update(dict(name = data['name'], brand=data['brand'], model = data['model'], 
                        voltage = data['voltage'], description = data['description'], 
                        is_active = data['is_active']))
        
        Sensor.query.filter_by(id=data['id'])\
                        .update(dict(is_active = data['is_active']))
        db.session.commit()