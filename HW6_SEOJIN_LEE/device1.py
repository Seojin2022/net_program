from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 10001))
s.listen(1)
print('Device1 is running...')

conn, addr = s.accept()
while True:
    msg = conn.recv(1024).decode()
    if msg == 'Request':
        temp = random.randint(0, 40)
        humid = random.randint(0, 100)
        illum = random.randint(70, 150)
        conn.send(f'{temp},{humid},{illum}'.encode())
    elif msg == 'quit':
        break

conn.close()
