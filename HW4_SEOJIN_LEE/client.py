import socket

def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 9000))

    print("간단 계산기 (예: 20+17 또는 20 + 17). 종료하려면 'q' 입력")
    while True:
        expr = input("계산식 입력: ")
        if expr.lower() == 'q':
            break

        sock.send(expr.encode())

        result = sock.recv(1024).decode()
        print("결과:", result)

    sock.close()

if __name__ == "__main__":
    main()
