from models import db, Device

class Actuator(db.Model):
    __tablename__ = "actuators"
    id = db.Column("id", db.ForeignKey(Device.id), primary_key=True)
    type = db.Column(db.String(25), nullable = False)
    
    activations = db.relationship("Activation", backref="actuators", lazy=True)