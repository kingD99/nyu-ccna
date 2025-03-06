from flask import Flask, request, jsonify
import requests
import socket

app = Flask(__name__)

def get_fs_ip(hostname, as_ip, as_port):
    message = f"TYPE=A\nNAME={hostname}\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(message.encode(), (as_ip, int(as_port)))
    sock.settimeout(2)
    
    try:
        data, _ = sock.recvfrom(1024)
        response = data.decode().split("\n")
        if "VALUE=" in response[2]:
            return response[2].split("=")[1].strip()
    except socket.timeout:
        return None
    return None

@app.route('/fibonacci', methods=['GET'])
def fibonacci_request():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not all([hostname, fs_port, number, as_ip, as_port]):
        return "Missing parameters", 400

    fs_ip = get_fs_ip(hostname, as_ip, as_port)
    if not fs_ip:
        return "Failed to resolve hostname", 400

    url = f"http://{fs_ip}:{fs_port}/fibonacci?number={number}"
    response = requests.get(url)

    return jsonify({"result": response.json()}) if response.status_code == 200 else ("Error", 400)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

