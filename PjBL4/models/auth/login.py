from models import db

class Login(db.Model):
    __tablename__ = "logins"
    id = db.Column("id",  db.Integer(), primary_key=True)
    username_email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(1024), nullable=False) 
    logged_at = db.Column(db.Date, nullable=False)

    # def __init__(self, username_email, password, logged_at):
    #     self.username_email = username_email
    #     self.password = generate_password_hash(password)
    #     self.logged_at = logged_at

    # def verify_password(self, pwd):
    #     return check_password_hash(self.password, pwd)
    
