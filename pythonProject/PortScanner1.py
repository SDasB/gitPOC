import socket

target_host = "192.168.109.129"

port = 1

while (int(port) != 0):
    port = int(input("Please enter port value.Enter 0 to quit: \n"))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target_host, port))
    if result == 0:
        print(f"Port {port} is open")
    sock.close()