from flask import Flask, request, jsonify
import socket
import json

app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    data = request.json
    hostname = data.get('hostname')
    ip = data.get('ip')
    as_ip = data.get('as_ip')
    as_port = data.get('as_port')

    if not (hostname and ip and as_ip and as_port):
        return "Bad Request", 400

    # Register hostname with Authoritative Server (AS)
    # Send a UDP message to AS to register the hostname

    return "Created", 201

@app.route('/fibonacci', methods=['GET'])
def fibonacci():
    number = request.args.get('number')

    try:
        number = int(number)
    except ValueError:
        return "Bad Request: Invalid number format", 400

    fib = [0, 1]
    for i in range(2, number + 1):
        fib.append(fib[-1] + fib[-2])

    return jsonify({"fibonacci": fib[number]}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9090)
