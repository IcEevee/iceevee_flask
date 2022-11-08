from flask import Flask, render_template
import json

app = Flask(__name__)

def get_data():
    with open("data.json", "r") as f:
        datas = json.load(f)
    return datas

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/book-generator')
def book_gen():
    return render_template('bookgenerator.html')

@app.route('/nilam-cnp')
def nilam_cnp():
    datas = get_data()
    return render_template('nilamcnp.html', datas=datas)