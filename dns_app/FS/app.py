from flask import Flask, request, jsonify
import socket
import json

app = Flask(__name__)
fs_ip = "172.18.0.2"  # This will be replaced by the container's actual IP
fs_port = 9090

@app.route('/register', methods=['PUT'])
def register():
    data = request.get_json()
    if not all(k in data for k in ("hostname", "ip", "as_ip", "as_port")):
        return "Invalid request", 400

    message = f"TYPE=A\nNAME={data['hostname']}\nVALUE={data['ip']}\nTTL=10\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (data['as_ip'], int(data['as_port'])))
    
    return "Registered", 201

def fibonacci(n):
    a, b = 0, 1
    for _ in range(int(n)):
        a, b = b, a + b
    return a

@app.route('/fibonacci', methods=['GET'])
def compute_fibonacci():
    number = request.args.get('number')
    if not number or not number.isdigit():
        return "Invalid number", 400
    return jsonify({"result": fibonacci(int(number))})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=fs_port)

