from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
            
@app.route('/orders')
def orders():
    return render_template('orders.html')

if __name__ == "__main__":
    app.run()
