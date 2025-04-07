from socket import *
import random

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 10002))
s.listen(1)
print('Device2 is running...')

conn, addr = s.accept()
while True:
    msg = conn.recv(1024).decode()
    if msg == 'Request':
        heart = random.randint(40, 140)
        steps = random.randint(2000, 6000)
        cal = random.randint(1000, 4000)
        conn.send(f'{heart},{steps},{cal}'.encode())
    elif msg == 'quit':
        break

conn.close()
