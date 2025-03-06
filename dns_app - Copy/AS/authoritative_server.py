import socket
import json

DNS_DB = {}

def handle_registration(data):
    # Parse registration data and store it in DNS_DB
    pass

def handle_query(query):
    # Handle DNS query and return registered IP address
    pass

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("0.0.0.0", 53533))

    while True:
        data, addr = server_socket.recvfrom(1024)
        # Handle incoming UDP packets (either registration or query)
        handle_registration(data) if b"TYPE=A" in data else handle_query(data)

if __name__ == "__main__":
    start_server()
