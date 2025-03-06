# Authoritative Server (AS)
# File: AS/auth_server.py

import socket

dns_records = {}

# UDP Server Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 53533))

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode().split('\n')
    
    if message[0] == "TYPE=A" and len(message) >= 3:
        if "VALUE=" in message[1]:  # Registration
            hostname = message[1].split('=')[1]
            ip_address = message[2].split('=')[1]
            dns_records[hostname] = ip_address
        else:  # Query
            hostname = message[1].split('=')[1]
            response = f"TYPE=A\nNAME={hostname}\nVALUE={dns_records.get(hostname, 'NOT_FOUND')}\nTTL=10\n"
            sock.sendto(response.encode(), addr)
