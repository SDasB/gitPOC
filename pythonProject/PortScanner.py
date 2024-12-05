import socket

target_host = "192.168.109.129"
start_port = 1
end_port = 1000

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    print(sock)
    result = sock.connect_ex((target_host, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()
