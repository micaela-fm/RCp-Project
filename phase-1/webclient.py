#WebClient.py

import socket

Message404 = "GET /nofilehere.html HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
Message400 = "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n"
Message200 = "GET /dashboard/index.html HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
Message302 = "GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"

print("WEB Client v0.2\n\n")
print("teste para obtenção de respostas do webserver\n\n")
print("o teste irá enviar uma mensagem GET para a porta 80 de um servidor à sua escolha, ")
print("formatada propositadamente para um determinado retorno.\n")
print("NOTA: O programa está desenhado para obter as respostas indicadas utilizando o XAMPP configurado por defeito como webserver.")

socketObject = socket.socket()
host = input("insira o host de onde pretende obter a mensagem de retorno: ")
socketObject.connect((host,80))

print("mensagens possíveis de obter:\n200 - OK\n302 - Found\n400 - Bad Request\n404 - Not Found")
msg = int(input("insira a mensagem de retorno que pretende, das indicadas acima: "))

valid = 0

if msg == 200:
    HTTPMessage = Message200
    valid = 1
elif msg == 400:
    HTTPMessage = Message400
    valid = 1
elif msg == 302:
    HTTPMessage = Message302
    valid = 1
elif msg == 404:
    HTTPMessage = Message404
    valid = 1
else:
    print("opção não reconhecida")

if valid == 1:
    #envio da mensagem:
    print("mensagem enviada: \n")
    print(HTTPMessage)
    message = str.encode(HTTPMessage)
    socketObject.sendall(message)

    #retorno:
    print("\nmensagem de retorno:\n")
    returnData = socketObject.recv(1024)
    print(returnData)

wait = input("\nPrima qualquer tecla para terminar")
socketObject.close()