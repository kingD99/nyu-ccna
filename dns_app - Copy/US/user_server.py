from flask import Flask, request, jsonify
import socket

app = Flask(__name__)

@app.route('/fibonacci', methods=['GET'])
def get_fibonacci():
    hostname = request.args.get('hostname')
    fs_port = request.args.get('fs_port')
    number = request.args.get('number')
    as_ip = request.args.get('as_ip')
    as_port = request.args.get('as_port')

    if not (hostname and fs_port and number and as_ip and as_port):
        return "Bad Request", 400

    try:
        number = int(number)
    except ValueError:
        return "Bad Request: Invalid Fibonacci number format", 400

    # Query DNS to resolve the hostname
    resolved_ip = socket.gethostbyname(hostname)

    # Send request to Fibonacci Server
    # Example: send GET request to FS at fs_ip:fs_port/fibonacci?number=X

    return jsonify({"fibonacci": number}), 200

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
