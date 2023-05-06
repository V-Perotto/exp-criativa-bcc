from models.db import db
from models import Product
from models import Ingredient

class ProductIngredients(db.Model):
    __tablename__ = 'product_ingredients'
    id = db.Column(db.Integer(), primary_key=True)
    product_id = db.Column(db.Integer(), db.ForeignKey(Product.id, ondelete='CASCADE'))
    ingredient_id = db.Column(db.Integer(), db.ForeignKey(Ingredient.id, ondelete='CASCADE'))