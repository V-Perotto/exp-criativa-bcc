from models import db, Sensor, User
from datetime import datetime

class Read(db.Model):
    __tablename__ = "reads"
    id = db.Column("id", db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    sensor_id = db.Column(db.Integer(), db.ForeignKey(Sensor.id))
    temp = db.Column(db.Float())
    umid = db.Column(db.Float())
    read_datetime = db.Column(db.DateTime(), nullable=False, default=datetime.now())

    def save_read(user_id, sensor_id, temp, umid):
        read = Read(user_id=user_id,
                    sensor_id=sensor_id,
                    temp=temp, 
                    umid=umid)
        
        db.session.add(read)
        db.session.commit()