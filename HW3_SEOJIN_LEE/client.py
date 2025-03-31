import socket
import struct

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)

# 서버 인사 메시지 수신
msg = sock.recv(1024)
print(msg.decode())

# 본인의 이름 전송 (문자열)
my_name = "Seojin Lee"
sock.send(my_name.encode())

# 학번 수신 (4바이트 고정 길이 받기)
data = sock.recv(4)
if len(data) < 4:
    print("Error: did not receive full 4 bytes of student ID")
else:
    # Big endian으로 변환하여 정수 출력
    student_id = struct.unpack('>I', data)[0]
    print("Received student ID:", student_id)

sock.close()
