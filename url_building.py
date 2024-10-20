from flask import Flask,url_for,redirect
# from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index1():
    return 'index'

@app.route('/login')
def login1():
    return 'login'

@app.route('/user/<username>')
def profile1(username):
    return f'{username}\'s profile'


    
@app.route('/url/bind/<int:age>')
def url_bind(age):
    if age < 18:
        return  redirect('/')
    # return "{url_for('index1')}"
    else:
        return f"hello your age is {age}"
