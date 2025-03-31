import socket
import re

def calculate(expression):
    try:
        # 공백 제거
        expression = expression.replace(" ", "")
        # 정규식으로 숫자와 연산자 분리
        match = re.match(r'(-?\d+)([+\-*/])(-?\d+)', expression)
        if not match:
            return "잘못된 입력입니다."

        a, op, b = match.groups()
        a = int(a)
        b = int(b)

        if op == '+':
            return str(a + b)
        elif op == '-':
            return str(a - b)
        elif op == '*':
            return str(a * b)
        elif op == '/':
            if b == 0:
                return "0으로 나눌 수 없습니다."
            return "{:.1f}".format(a / b)
        else:
            return "지원하지 않는 연산자입니다."
    except Exception as e:
        return f"에러 발생: {str(e)}"

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('', 9000))
    server.listen(1)
    print("서버가 실행 중입니다. 연결을 기다리는 중...")

    client, addr = server.accept()
    print("클라이언트 연결:", addr)

    while True:
        data = client.recv(1024)
        if not data:
            break
        expression = data.decode()
        print("수신된 계산식:", expression)

        result = calculate(expression)
        client.send(result.encode())

    client.close()
    server.close()

if __name__ == "__main__":
    main()
