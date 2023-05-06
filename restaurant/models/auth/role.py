from models import db

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column("id",db.Integer(), primary_key=True)
    name = db.Column(db.String(45))
    description = db.Column(db.String(512))
    
    users = db.relationship('User',back_populates = "roles", secondary = 'users_roles')