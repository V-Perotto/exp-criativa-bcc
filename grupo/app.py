from flask import Flask, render_template, session, g, url_for

from controllers.admin_controller import admin
from controllers.iot_controller import iot
from controllers.user_controller import user

app = Flask(__name__, template_folder="./views/", static_folder="./static/")

app.register_blueprint(admin, url_prefix='/admin')
app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(iot, url_prefix='/IoT')

@app.route('/')
def index():
    return render_template("base.html")

if __name__ == "__main__":
    app.run(debug=True)