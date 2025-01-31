import os
import json
from flask import Flask, jsonify

app = Flask(__name__)

# Define the path to data.json
data_file = os.path.join(os.path.dirname(__file__), 'data.json')

# Load the data
try:
    with open(data_file) as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}  # Use an empty dictionary if the file is missing

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/stats')
def stats():
    return jsonify(data)  # Return the JSON data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)


