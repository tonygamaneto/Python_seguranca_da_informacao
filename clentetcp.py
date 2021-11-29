import socket
import sys


def main():
    try:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('\033[1;32mA Conexao Falhou !!\033[1;m')
        print('ERRO : {} '.format(e))
        sys.exit()
    print('\033[1;34mSocket Criado com sucesso !!\033[1;m')

    Hostalvo = input('Digite o Host ou IP a ser conectado: ')
    Portaalvo = input('Digite o numero da  porta a ser conectada: ')

    try:
        s.connect((Hostalvo, int(Portaalvo)))
        print('\033[1;32mCliente TCP conectado com sucesso no Host:\033[1;m ' + Hostalvo + ' \033[1;32me na porta\033[1;m '+ Portaalvo)
        s.shutdown(2)
    except socket.error as e:
        print('\033[1;31mnao foi possivel conectar no \033[1;m ' + Hostalvo + '\033[1;31m e nem na porta\033[1;m '+ Portaalvo)
        print('ERRO : {}'.format(e))
        sys.exit()
if __name__ == "__main__":
    main()
