from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/calculator/greeting', methods=['GET'])
def greeting():
    return "Hello, world!",200

@app.route('/calculator/add', methods=['POST'])
def add():
    data = request.json
    first = data.get('first')
    second = data.get('second')

    if first is None or second is None:
        return jsonify({"error": "Missing 'first' or 'second' parameter"}), 400

    result = first + second
    return jsonify({"result": result}),200

@app.route('/calculator/subtract', methods=['POST'])
def subtract():
    data = request.json
    first = data.get('first')
    second = data.get('second')

    if first is None or second is None:
        return jsonify({"error": "Missing 'first' or 'second' parameter"}), 400

    result = first - second
    return jsonify({"result": result}),200

if __name__ == '__main__':
    app.run()
