from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>Index Page</h2>'

@app.route('/h')
def index1():
    return "<h1>Hello</h1>"