from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/data")
def get_data():
    return jsonify({"data":"01/01/2024"})

if __name__ == '__main__':
    app.run(debug=True)