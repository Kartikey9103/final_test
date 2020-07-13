from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! try again second time"

@app.route('/test/<string:data>', methods=['GET'])
def hellotest(data):
    return data
