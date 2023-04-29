from models import db, Actuator, User
from datetime import datetime

class Activation(db.Model):
    __tablename__ = 'activations'
    id = db.Column("id", db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id))
    actuator_id = db.Column(db.Integer(), db.ForeignKey(Actuator.id))

    activation_datetime = db.Column(db.DateTime(), nullable = False, default=datetime.now())