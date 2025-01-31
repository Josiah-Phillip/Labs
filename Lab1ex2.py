from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/add/<int:a>/<int:b>', methods=['GET'])
def add(a, b):
    return jsonify({'result': a + b})

@app.route('/subtract/<int:a>/<int:b>', methods=['GET'])
def subtract(a, b):
    return jsonify({'result': a - b})

@app.route('/multiply/<int:a>/<int:b>', methods=['GET'])
def multiply(a, b):
    return jsonify({'result': a * b})

@app.route('/divide/<int:a>/<int:b>', methods=['GET'])
def divide(a, b):
    if b == 0:
        return jsonify({'error': 'Division by zero is not allowed'}),

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
