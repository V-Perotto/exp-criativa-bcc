from datetime import datetime
from models import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = "users"
    id = db.Column("id",  db.Integer(), primary_key=True)
    email = db.Column(db.String(30), nullable=False, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False) 
    is_admin = db.Column(db.Boolean)
    created_at = db.Column(db.Date, nullable=False, default=datetime.now())

    def get_user():
        users = User.query.add_columns(User.id, 
                                       User.email, 
                                       User.username,
                                       User.is_admin, 
                                       User.created_at).all()
        return users
    
    def save_user(email, username, password, is_admin):
        user = User(email=email, 
                    username=username, 
                    password=password,
                    is_admin=is_admin)
        
        db.session.add(user)
        db.session.commit()

    def delete_user(user_id):
        user = User.query.get(user_id)
        db.session.delete(user)
        db.session.commit()

    def update_user(data):
        User.query.filter_by(id=data['id'])\
            .update(dict(email = data['email'], username = data['username'], 
                         password = data['password'], is_admin = data['is_admin']))
    
        db.session.commit()
