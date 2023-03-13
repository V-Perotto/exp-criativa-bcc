from flask import Flask, render_template

app = Flask(__name__)

## __name__ is the application name
@app.route('/')
def index():
    return render_template('html/home.html')

@app.route('/orders')
def orders():
    pedidos = ["Combo 1, comanda 2","Executivo 2, comanda 3",
                "Refri laranja, comanda 134","Cerveja, comanda 12",
                "Batata Frita, comanda 14"]
    return render_template("html/orders.html", orders = pedidos)

if __name__ == '__main__':
    app.run(host='14.0.0.1', port="05", debug=True)

