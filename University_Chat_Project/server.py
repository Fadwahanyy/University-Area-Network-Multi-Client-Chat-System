import socket
import threading

def handle_client(conn, addr):
    while True:
        try:
            message = conn.recv(1024)
            if not message: break
            # Broadcast to all clients
            for client in clients:
                if client != conn:
                    client.send(message)
        except: break
    conn.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 65432)) # Local testing IP
server.listen()
clients = []
print("SERVER IS RUNNING...")

while True:
    conn, addr = server.accept()
    clients.append(conn)
    threading.Thread(target=handle_client, args=(conn, addr)).start()