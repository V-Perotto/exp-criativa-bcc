from flask import Blueprint, render_template, request, redirect, url_for
from models import Billing, BillingForm

billing = Blueprint("billing", __name__, template_folder='./views/admin/', static_folder='./static/', root_path="./")

@billing.route("/")
def billing_index():
    return render_template("/billing/billing_index.html")

@billing.route("/register_billing_form", methods=["GET", "POST"])
def register_billing_form():
    name = request.form.get("name")
    description = request.form.get("description")
    
    BillingForm.set_billing_form(name, description)

    return render_template("/billing/register_billing_forms.html")

@billing.route("/register_billing", methods=["GET", "POST"])
def register_billing():
    value = request.form.get("value")
    billing_date = request.form.get("billing_date")

    Billing.set_billing(value, billing_date)

    return render_template("/billing/register_billing.html")

@billing.route("/view_billing_forms")
def view_billing_forms():
    return render_template("/billing/view_billing_forms.html", billing_forms = BillingForm.get_billing_form())

@billing.route("/view_billings")
def view_billings():
    return render_template("/billing/view_billing.html")