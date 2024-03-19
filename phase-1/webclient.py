# WebClient.py

import socket

HTTP_MESSAGES = {
    200: "GET /dashboard/index.html HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n",
    302: "GET / HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n",
    400: "GET / HTTP/1.1\r\nHost: localhost\r\n Connection: close\r\n\r\n",
    404: "GET /nofilehere.html HTTP/1.1\r\nHost: localhost\r\nConnection: close\r\n\r\n"
}

def send_message(socket_object, message):
    print("mensagem enviada: \n")
    print(message)
    encoded_message = str.encode(message)
    socket_object.sendall(encoded_message)

    print("\nmensagem de retorno:\n")
    return_data = socket_object.recv(1024)
    print(return_data)

print("WEB Client v0.2\n\n")
print("teste para obtenção de respostas do webserver\n\n")
print("o teste irá enviar uma mensagem GET para a porta 80 de um servidor à sua escolha, ")
print("formatada propositadamente para um determinado retorno.\n")
print("NOTA: O programa está desenhado para obter as respostas indicadas utilizando o XAMPP configurado por defeito como webserver.")

socket_object = socket.socket()
host = input("insira o host de onde pretende obter a mensagem de retorno: ")
socket_object.connect((host,80))

print("mensagens possíveis de obter:\n200 - OK\n302 - Found\n400 - Bad Request\n404 - Not Found")

while True:
    try:
        msg = int(input("insira a mensagem de retorno que pretende, das indicadas acima: "))
        http_message = HTTP_MESSAGES[msg]
        break
    except KeyError:
        print("opção não reconhecida")

send_message(socket_object, http_message)

wait = input("\nPrima qualquer tecla para terminar")
socket_object.close()
