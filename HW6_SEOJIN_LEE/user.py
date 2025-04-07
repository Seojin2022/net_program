from socket import *
import time

dev1 = socket(AF_INET, SOCK_STREAM)
dev1.connect(('localhost', 10001))

dev2 = socket(AF_INET, SOCK_STREAM)
dev2.connect(('localhost', 10002))

f = open('data.txt', 'w')

while True:
    cmd = input("Enter 1/ 2/ quit: ")
    now = time.ctime(time.time())

    if cmd == '1':
        dev1.send(b'Request')
        data = dev1.recv(1024).decode()
        temp, humid, illum = data.split(',')
        f.write(f'{now}: Device1: Temp={temp}, Humid={humid}, Illum={illum}\n')
        print("Device1 data saved.")

    elif cmd == '2':
        dev2.send(b'Request')
        data = dev2.recv(1024).decode()
        heart, steps, cal = data.split(',')
        f.write(f'{now}: Device2: Heartbeat={heart}, Steps={steps}, Cal={cal}\n')
        print("Device2 data saved.")

    elif cmd == 'quit':
        dev1.send(b'quit')
        dev2.send(b'quit')
        break

f.close()
dev1.close()
dev2.close()
