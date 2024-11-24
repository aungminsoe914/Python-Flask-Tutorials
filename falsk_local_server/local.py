from flask import Flask

app = Flask(__name__)

@app.route('/')
def upload_form():
    return "Hello world"

if __name__ == '__main__':
    # Run the app on address '0.0.0.0' and port 8090
    app.run(host='0.0.0.0', port=8090, debug=True)
    
    
    
    
    #  ? ! important sudo ufw allow 8090

