from models import db, User, Sensor

class Read(db.Model):
    __tablename__ = 'reads'
    id = db.Column(db.Integer(), primary_key=True)
    id_user = db.Column(db.Integer(),db.ForeignKey(User.id), nullable = False)
    id_sensor = db.Column(db.Integer(),db.ForeignKey(Sensor.id), nullable = False)
    value = db.Column(db.Float(), nullable = False)
    date_time = db.Column(db.DateTime(), nullable = False)
    
    users = db.relationship("Users", backref="users", lazy= True)