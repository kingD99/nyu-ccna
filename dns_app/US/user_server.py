# User Server (US)
# File: US/user_server.py

from flask import Flask, request, jsonify
import requests
import socket

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')
    
    if not all([hostname, fs_port, number, as_ip, as_port]):
        return "Missing parameters", 400
    
    # Query AS for the IP address of hostname
    query_msg = f"TYPE=A\nNAME={hostname}\n"
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(query_msg.encode(), (as_ip, int(as_port)))
    
    response, _ = sock.recvfrom(1024)
    sock.close()
    
    response_lines = response.decode().split('\n')
    if len(response_lines) < 3 or not response_lines[1].startswith("VALUE="):
        return "DNS lookup failed", 404
    
    fs_ip = response_lines[1].split('=')[1]
    
    # Request Fibonacci number from FS
    fibonacci_url = f"http://{fs_ip}:{fs_port}/fibonacci?number={number}"
    fibonacci_response = requests.get(fibonacci_url)
    
    return jsonify(fibonacci_response.json()), fibonacci_response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
