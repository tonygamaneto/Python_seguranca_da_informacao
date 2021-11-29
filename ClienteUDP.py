import socket
import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('\033[1;34mCliente Socket criado com SUCESSO !!\033[1m')
host =  'localhost'
porta = 5433
mensagem =  'Ola Servidor firmeza ?'

try:
    print('Cliente : ' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print('cliente enviou : ' + dados )
finally:
    print('cliente fechando a conexao')
    s.close()