from flask import Flask, render_template

app = Flask(__name__)

# ...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/load_data')
def load_data():
    result = ativos()
    return result

def ativos():
    return 1
# ...
