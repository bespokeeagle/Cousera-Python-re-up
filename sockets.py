import socket

testsock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
testsock.connect(('data.pr4e.org',80))
cmd = "GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n" .encode()

testsock.send(cmd)

while True:
    data = testsock.recv(1024)
    if len(data) < 1:
        break
    print (data.decode(),end="")
testsock.close()
