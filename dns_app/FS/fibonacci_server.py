# Fibonacci Server (FS)
# File: FS/fibonacci_server.py

from flask import Flask, request, jsonify
import socket
import json

def fibonacci(n):
    if n == 0: return 0
    elif n == 1: return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

app = Flask(__name__)

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    hostname = data.get("hostname")
    ip = data.get("ip")
    as_ip = data.get("as_ip")
    as_port = data.get("as_port")
    
    if not all([hostname, ip, as_ip, as_port]):
        return "Missing parameters", 400
    
    registration_msg = f"TYPE=A\nNAME={hostname}\nVALUE={ip}\nTTL=10\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(registration_msg.encode(), (as_ip, int(as_port)))
    sock.close()
    
    return "Registered successfully", 201

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    number = request.args.get("number")
    if not number.isdigit():
        return "Invalid input", 400
    
    result = fibonacci(int(number))
    return jsonify({"result": result}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
