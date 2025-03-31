import socket
import struct

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    print('Connection from', addr)

    # 인사 메시지 전송
    client.send(b'Hello ' + addr[0].encode())

    # 학생의 이름 수신
    name = client.recv(1024).decode()
    print(name)

    # 학번 전송 (정수값 -> 엔디언 변환 -> 전송)
    student_id = 20221308  # 예시 학번
    data = struct.pack('>I', student_id)  # Big endian으로 변환
    client.send(data)

    client.close()
