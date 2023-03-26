from flask import Flask, render_template

app = Flask(__name__)

hrefs = ["/orders", "/clients", "/employee"]
descriptions = ["Listar Pedidos","Listar Clientes", "Listar Funcionários"]
    

@app.route('/')
def index():
    return render_template('index.html', hrefs=hrefs, descriptions=descriptions)
            
@app.route('/orders')
def orders():
    orders_list = ["Combo 1, comanda 2","Executivo 2, comanda 3", 
                   "Refri laranja, comanda 134","Cerveja, comanda 12",
                   "Batata Frita, comanda 14"]

    return render_template('orders.html', orders_list = orders_list)

if __name__ == "__main__":
    app.run()
