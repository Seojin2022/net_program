import socket
import threading

def handler(sock):
    while True:
        try:
            msg = sock.recv(1024)
            if not msg:
                break
            print(msg.decode())
        except:
            break

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 2500))

my_id = input('ID를 입력하세요: ')
sock.send(f'[{my_id}]'.encode())

th = threading.Thread(target=handler, args=(sock,))
th.daemon = True
th.start()

while True:
    msg = input()
    if msg.lower() == 'quit':
        sock.send(f'[{my_id}] 퇴장'.encode())
        break
    sock.send(f'[{my_id}] {msg}'.encode())

sock.close()
