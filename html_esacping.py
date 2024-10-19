from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/<name>')
def hello(name):
    return f"Hello, {escape(name)}"


# ? run
    """
    flask --app <your_python_name>  run
    
    127.0.0.1:5000/entername
    """
