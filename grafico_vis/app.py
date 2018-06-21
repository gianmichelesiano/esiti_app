from flask import Flask
app = Flask(__name__)
from flask import jsonify
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    with open('data1.json') as f:
        data = json.load(f)
    return jsonify(data)    
    #return 'Hello, Wrfeorld!'

@app.route('/')
def hello_world():
    with open('data1.json') as f:
        data = json.load(f)

    return jsonify(data)  

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5000,debug=True)
