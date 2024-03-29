from models import db, User, Role

class UserRole(db.Model):
    __tablename__ = 'user_roles'
    user_id = db.Column(db.Integer(), db.ForeignKey(User.id),primary_key=True)
    role_id = db.Column(db.Integer(), db.ForeignKey(Role.id),primary_key=True)