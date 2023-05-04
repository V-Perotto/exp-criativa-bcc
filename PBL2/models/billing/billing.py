from models.db import db

class Billing(db.Model):
    __tablename__ = 'billings'
    id = db.Column('id', db.Integer, primary_key=True)
    value = db.Column(db.Float)
    billing_date = db.Column(db.DateTime)

    billing_forms = db.relationship('BillingForm', back_populates = "billings", secondary='billing_billing_forms')

    def set_billing(value, billing_date):
        billing_form = Billing(value = value, billing_date = billing_date)

        # billing_billing_form add?

        db.session.add(billing_form)
        db.session.commit()

    def get_billing():
        billing_form = Billing.query.join(
                            Billing, 
                            Billing.id == id
                            ).add_columns(
                                Billing.value,
                                Billing.billing_date
                                )
        
        return billing_form