from models import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column("id",db.Integer(), primary_key=True)
    username = db.Column(db.String(45))
    password = db.Column(db.String(512))
    
    roles = db.relationship('Role',back_populates = "users", secondary = 'users_roles')
    reads = db.relationship('Read',backref='users', lazy=True)
    activations = db.relationship("Activation", backref="users", lazy=True)
    