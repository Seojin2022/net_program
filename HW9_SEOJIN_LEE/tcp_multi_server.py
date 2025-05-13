import socket
import threading
import time

svr_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_sock.bind(('0.0.0.0', 2500))
svr_sock.listen()
print('Server Started')

clients = []

def client_handler(conn, addr):
    print('new client', addr)
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            log = time.asctime() + str(addr) + ':' + msg.decode()
            print(log)

            for client in clients:
                if client != conn:
                    client.send(msg)
        except:
            break
    print(addr, 'disconnected')
    clients.remove(conn)
    conn.close()

while True:
    conn, addr = svr_sock.accept()
    clients.append(conn)
    th = threading.Thread(target=client_handler, args=(conn, addr))
    th.daemon = True
    th.start()
