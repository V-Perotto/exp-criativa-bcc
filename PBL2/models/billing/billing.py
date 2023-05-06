from models.db import db

class Billing(db.Model):
    __tablename__ = 'billings'
    id = db.Column('id', db.Integer, primary_key=True)
    value = db.Column(db.Float)
    billing_date = db.Column(db.DateTime)

    billing_forms = db.relationship('BillingForm', back_populates = "billings", secondary='billing_billing_forms')

    def set_billing(value, billing_date):
        billing = Billing(value = value, billing_date = billing_date)

        db.session.add(billing)
        db.session.commit()

    def get_billing():
        return Billing.query.all()