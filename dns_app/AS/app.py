import socket
import os

db_file = "dns_records.txt"

def save_dns_record(hostname, ip):
    # Ensure the file exists before writing
    if not os.path.exists(db_file):
        with open(db_file, "w") as f:
            pass  # Create an empty file

    with open(db_file, "a") as f:
        f.write(f"{hostname} {ip}\n")
        f.flush()  # Force write to disk immediately




def lookup_dns(hostname):
    try:
        with open(db_file, "r") as f:
            for line in f:
                name, ip = line.strip().split()
                if name == hostname:
                    return ip
    except FileNotFoundError:
        return None
    return None

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 53533))

print("Authoritative Server is running on UDP port 53533...")

while True:
    data, addr = sock.recvfrom(1024)
    message = data.decode().split("\n")
    print("Received DNS request:", message)


    if "VALUE=" in message[2] and "TTL=" in message[3]:  # Ensure correct registration format
        hostname = message[1].split("=")[1]
        ip = message[2].split("=")[1]
        save_dns_record(hostname, ip)
        print(f"Registered: {hostname} -> {ip}")
    else:  # DNS Query
        hostname = message[1].split("=")[1]
        ip = lookup_dns(hostname)
        response = f"TYPE=A\nNAME={hostname}\nVALUE={ip if ip else 'Not Found'}\nTTL=10\n"
        sock.sendto(response.encode(), addr)

