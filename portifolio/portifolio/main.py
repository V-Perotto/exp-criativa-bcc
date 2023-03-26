from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__, template_folder="./")

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(host='127.0.0.1', port="5000", debug=True)

