from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

registered_orders = []
clients_list = []
employees_list = []

hrefs = ["/orders", "/clients", "/employees", "/register_orders"]
descriptions = ["Listar Pedidos","Listar Clientes", "Listar Funcionários", "Registrar Pedidos"]
    
@app.route('/')
def index():
    return render_template('index.html', hrefs=hrefs, descriptions=descriptions)
            
@app.route('/orders')
def orders():
    global registered_orders
    return render_template('orders.html', hrefs=hrefs, descriptions=descriptions, orders_list = registered_orders)

@app.route('/clients')
def clients():
    return render_template('clients.html', hrefs=hrefs, descriptions=descriptions, clients_list=clients_list)

@app.route('/employees')
def employees():
    return render_template('employees.html', hrefs=hrefs, descriptions=descriptions, employees_list=employees_list)

@app.route('/register_orders')
def register_orders():
    return render_template("register_orders.html", hrefs=hrefs, descriptions=descriptions)

@app.route('/save_order', methods=['POST', 'GET'])
def save_order():
    product_name = request.form.get("product_name", None)
    ticket_id = request.form.get("ticket_id", None)
    
    global registered_orders
    registered_orders.append(f"{product_name}, comanda {ticket_id}")
    return redirect(url_for("orders"))

if __name__ == "__main__":
    app.run()
