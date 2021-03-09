from flask import Flask, render_template, send_from_directory, request, session
import mapper as mp

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/added', methods=['POST', 'GET'])
def add():
    result = 0

    if request.method == 'POST':
        req = request.form

        number1 = int(req.get('number1'))
        number2 = int(req.get('number2'))

        result = number1 + number2 * mp.return_age('Sofie')

        mp.change_age('Sofie', result)

    return render_template("index.html", result=result)