from flask import Flask

app = Flask(__name__)

@app.route("/page/")
def page():
    return "This is page"

@app.route("/about")
def about():
    return "This is about"