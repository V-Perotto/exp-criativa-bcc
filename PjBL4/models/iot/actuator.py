from models import db, Device

class Actuator(db.Model):
    __tablename__ = "actuators"
    id = db.Column("id", db.ForeignKey(Device.id), primary_key=True)
    type = db.Column(db.String(20), nullable=False)

    activations = db.relationship("Activation", backref="actuators", lazy=True)
        
    def save_actuator_2(name, model, brand, convenient, description, is_active, type):
        device = Device(name = name, model = model, brand = brand, convenient = convenient, description = description, 
                        is_active = is_active)
        
        actuator = Actuator(id=device.id, type=type)
        device.actuators.append(actuator)
        
        db.session.add(device)
        db.session.commit()
        
    def get_actuators():
        actuators = Actuator.query.join(Device, Device.id == Actuator.id)\
                        .add_columns(Device.id, Device.name, Device.model, Device.brand, Device.convenient, Device.description,
                                     Device.is_active, Actuator.type).all()
        return actuators