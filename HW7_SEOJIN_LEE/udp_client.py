from socket import *

client = socket(AF_INET, SOCK_DGRAM) 
server_address = ('localhost', 9999)

while True:
    msg = input('Enter command" ("send mboxId message" or "receive mboxId"): ')
    client.sendto(msg.encode(), server_address)

    if msg == "quit":   
        print("Client exiting.") 
        break 

    data, _ = client.recvfrom(1024)
    print("Server response:", data.decode())

client.close()
