from flask import Flask, render_template

app = Flask(__name__)

## __name__ is the application name
@app.route('/')
def index():
    return render_template('html/home.html')

@app.route('/orders')
def orders():
    return render_template("html/orders.html")

if __name__ == '__main__':
    app.run(host='14.0.0.1', port="05", debug=True)

