from socket import *

mbox = {}  
server = socket(AF_INET, SOCK_DGRAM)
server.bind(('', 9999)) 
print("UDP Server is running...")

while True:
    data, addr = server.recvfrom(1024)
    msg = data.decode()

    if msg.startswith("send "):
        parts = msg.split(' ', 2) 
        if len(parts) < 3:
            server.sendto(b"Invalid format", addr)
            continue
        mbox_id = parts[1]
        message = parts[2]

        if mbox_id not in mbox:
            mbox[mbox_id] = []
        mbox[mbox_id].append(message)

        server.sendto(b"OK", addr)

    elif msg.startswith("receive "):
        parts = msg.split()
        if len(parts) != 2:
            server.sendto(b"Invalid format", addr)
            continue
        mbox_id = parts[1]

        if mbox_id in mbox and mbox[mbox_id]:
            msg_to_send = mbox[mbox_id].pop(0)
            server.sendto(msg_to_send.encode(), addr)
        else:
            server.sendto(b"No messages", addr)

    elif msg == "quit":
        print("Server shutting down.")
        break  
 

    else:
        server.sendto(b"Unknown command", addr)

server.close()
