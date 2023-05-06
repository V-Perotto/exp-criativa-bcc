from models.db import db
from models import Billing
from models import BillingForm

class BillingBillingForms(db.Model):
    __tablename__ = 'billing_billing_forms'
    id = db.Column(db.Integer(), primary_key=True)
    billing_id = db.Column(db.Integer(), db.ForeignKey(Billing.id, ondelete='CASCADE'))
    billing_form_id = db.Column(db.Integer(), db.ForeignKey(BillingForm.id, ondelete='CASCADE'))
    value = db.Column(db.Float())

    def set_billing_billing_forms(billing_id, billing_form_id, value):
        billing_billing_forms = BillingBillingForms(billing_id = billing_id, billing_form_id = billing_form_id, value = value)
    
        db.session.add(billing_billing_forms)
        db.session.commit()

    def get_billing_billing_forms():
        billing_billing_form = BillingBillingForms.query.all()
        return billing_billing_form