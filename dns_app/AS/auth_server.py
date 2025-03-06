import socket

dns_records = {}

# UDP Server Setup
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 53533))

print("AS is running and listening on UDP port 53533...")  # Debugging output

while True:
    data, addr = sock.recvfrom(1024)
    print(f"Received message from {addr}: {data.decode()}")  # Debugging output

    message = data.decode().split('\n')

    if message[0] == "TYPE=A" and len(message) >= 3:
        if "VALUE=" in message[1]:  # Registration
            hostname = message[1].split('=')[1]
            ip_address = message[2].split('=')[1]
            dns_records[hostname] = ip_address
            print(f"Registered {hostname} -> {ip_address}")  # Debugging output
        else:  # Query
            hostname = message[1].split('=')[1]
            response = f"TYPE=A\nNAME={hostname}\nVALUE={dns_records.get(hostname, 'NOT_FOUND')}\nTTL=10\n"
            print(f"Responding to query for {hostname}: {response.strip()}")  # Debugging output
            sock.sendto(response.encode(), addr)

