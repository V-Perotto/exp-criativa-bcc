from flask import Flask, render_template
import os
from pathlib import Path

ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent
CURDIR = os.getcwd()
TEMPLATE_DIR = os.path.join(CURDIR, "templates")
TEMPLATE_HTML_DIR = os.path.join(TEMPLATE_DIR, "html")

app = Flask(__name__, template_folder=TEMPLATE_HTML_DIR)

# web
@app.route('/')
def index():
    return render_template("home.html")

@app.route('/orders')
def orders():
    pedidos = ["Combo 1, comanda 2","Executivo 2, comanda 3",
                "Refri laranja, comanda 134","Cerveja, comanda 12",
                "Batata Frita, comanda 14"]
    return render_template("orders.html", orders = pedidos)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port="05", debug=True)

