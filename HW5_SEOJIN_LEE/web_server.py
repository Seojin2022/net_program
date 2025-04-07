from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    # 웹 서버 코드 작성
    # 각 객체(파일 또는 문자열) 전송 후, 소켓 닫기(c.close())

    print("요청:", req[0]) 

    try:
        filename = req[0].split()[1][1:]
    except:
        filename = 'index.html'

    if filename == '':
        filename = 'index.html'

    try:
        if filename == 'index.html':
            f = open('index.html', 'r', encoding='utf-8')
            mimeType = 'text/html'
            data = f.read()
            f.close()

            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'

            c.send(header.encode())
            c.send(data.encode('euc-kr')) 

        elif filename == 'iot.png':
            f = open(filename, 'rb')
            mimeType = 'image/png'
            data = f.read()
            f.close()

            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'

            c.send(header.encode())
            c.send(data)

        elif filename == 'favicon.ico':
            f = open(filename, 'rb')
            mimeType = 'image/x-icon'
            data = f.read()
            f.close()

            header = 'HTTP/1.1 200 OK\r\n'
            header += 'Content-Type: ' + mimeType + '\r\n'
            header += '\r\n'

            c.send(header.encode())
            c.send(data)

        else:
            raise FileNotFoundError

    except:
        response = 'HTTP/1.1 404 Not Found\r\n'
        response += '\r\n'
        response += '<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>'
        response += '<BODY>Not Found</BODY></HTML>'
        c.send(response.encode())

    c.close()