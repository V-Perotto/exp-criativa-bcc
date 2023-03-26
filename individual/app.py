from flask import Flask, render_template, session, g
from controllers.product_controller import product

app = Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(product, url_prefix='/product')

@app.route('/')
def index():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)