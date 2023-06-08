from models import db, Device, Sensor

class Convenient(db.Model):
    __tablename__ = "convenient"
    id = db.Column("id", db.Integer(), db.ForeignKey(Device.id), primary_key=True)
        
    def get_convenient():
        convenients = Convenient.query.join(Device, Device.id == Sensor.id)\
                    .add_columns(Device.name, Device.brand, Device.model, 
                                 Device.convenient, Device.description,  Device.is_active, Device.convenient).all()
        
        return convenients