from models import db, Device

class Sensor(db.Model):
    __tablename__ = "sensors"
    id = db.Column("id", db.ForeignKey(Device.id), primary_key=True)
    measure = db.Column(db.String(20), nullable = False)
    
    reads = db.relationship("Sensor", backref="sensors", lazy=True)

    def save_sensor(name, model, brand, voltage, description, is_active, measure):
        device = Device(name=name, model=model, brand=brand, voltage=voltage, description=description, is_active=is_active)

        db.session.add(device)
        db.session.commit()

        sensor = Sensor(id = device.id, measure=measure)

        db.session.add(sensor)
        db.session.commit()

    def save_sensor_alt(name, model, brand, voltage, description, is_active, measure):
        device = Device(name=name, model=model, brand=brand, voltage=voltage, description=description, is_active=is_active)

        sensor = Sensor(id = device.id, measure=measure)

        device.sensors.append(sensor)

        db.session.add(sensor)
        db.session.commit()

    def get_sensors():
        sensors = Sensor.query.join(
                                Device, 
                                Device.id == Sensor.id
                                ).add_columns(
                                            Device.id, Device.name, Device.model,
                                            Device.brand, Device.voltage, Device.description,
                                            Device.is_active, Sensor.measure).all()
        return sensors