import socket

s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
print('\033[1;34mSocket criado com SUCESSO !!\033[1m')

host = 'localhost'
porta = 5432

s.bind((host, porta))

mensagem = '\nservidor : Olá Cliente e aí beleza ?'

while 1:
    dados, end = s.recvfrom(4096)
    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)