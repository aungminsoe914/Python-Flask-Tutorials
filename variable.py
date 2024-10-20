from flask import Flask
from markupsafe import escape

app = Flask(__name__)

#escape route
@app.route("/user/<username>")
def var1(username):
    return f"Hello {escape(username)}"
#integer route
@app.route("/post/<int:post_id>")
def var2(post_id):
    return f"Post id integer {escape(post_id)}"

#route for subpath path
@app.route("/path/<path:subpath>")
def var3(subpath):
    return f"Sub Path {escape(subpath)}"

#route for float
@app.route("/count/<float:count_num>")
def count(count_num):
    return f"Count Float is {escape(count_num)}"

#route for uuid
"""
    uuid
    
    UUID looks like this: 123e4567-e89b-12d3-a456-426614174000, 
    which consists of 32 hexadecimal digits displayed in 
        five groups 
    separated by hyphens.
"""
@app.route("/uuid/<uuid:uuid_name>")
def uuid(uuid_name):
    return f"UUid is {escape(uuid_name)}"

