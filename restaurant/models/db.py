from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# instance = 'sqlite:///restaurant'
instance = "mysql+pymysql://root:6908@localhost:3306/new_restaurant"