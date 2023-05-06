from models.db import db

class Ingredient(db.Model):
    __tablename__ = "ingredients"
    id = db.Column(db.Integer, primary_key=True) # primary keys are required by SQLAlchemy
    name = db.Column(db.String(50))
    available_quantity = db.Column(db.Integer)

    products = db.relationship('Product', back_populates = "ingredients", secondary='product_ingredients')