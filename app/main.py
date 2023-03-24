from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder="./templates/html/")

registered = []

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/orders')
def orders():
    global registered
    return render_template("orders.html", orders = registered)

@app.route('/register_order', methods = ['POST', 'GET'])
def register_order():
    return render_template("register_order.html")

@app.route('/save_order', methods = ['POST', 'GET'])
def save_order():
    if request.method == 'POST':
        name = request.form['name']
        ticket = request.form['ticket']
    else:
        name = request.form.get('name', None)
        ticket = request.form.get('ticket', None)
    
    global registered
    registered.append(f"{name}, comanda {ticket}")
    # id = len(registered)+1
    # registered[id] = f"{name}, comanda {ticket}"
    
    return redirect(url_for("orders"))

if __name__ == '__main__':
    app.run(host='127.0.0.1', port="5000", debug=True)

