from models import db, Device, Sensor

class Convenient(db.Model):
    __tablename__ = "convenient"
    id = db.Column("id", db.Integer(), db.ForeignKey(Device.id), primary_key=True)
        
    def get_convenient():
        convenients = Convenient.query.join(Device, Device.id == Sensor.id)\
                    .add_columns(Device.name, Device.brand, Device.model, 
                                 Device.convenient, Device.description,  Device.is_active, Device.convenient).all()
        
        return convenients
    
    def update_convenient(data):
        Device.query.filter_by(id=data['id'])\
                .update(dict(name = data['name'], brand=data['brand'], model = data['model'], 
                        voltage = data['voltage'], description = data['description'], 
                        is_active = data['is_active']))
        
        Sensor.query.filter_by(id=data['id']).update(dict(is_active = data['is_active']))
        db.session.commit()