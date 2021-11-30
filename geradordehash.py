import hashlib

menu=1
while menu !=0:
    string = input('Digite o texto a ser gerado a HASH :  ')



    menu =  int(input('''  ##### ESCOLHA O TIPO DE HASH #####
                        1) MD5
                        2) SHA1
                        3) SHA256
                        4) SHA512
                        0) DIGITE (0) PARA SAIR
                        
                        -Digite o número da opção : '''))

    if menu ==1:
        resultado = hashlib.md5(string.encode())
        print('o hash da String :', string, 'é em MD5: ',  resultado.hexdigest())
    elif menu == 2:
        resultado = hashlib.sha1(string.encode())
        print('o hash da String :', string, 'é em SHA1: ', resultado.hexdigest())

    elif menu == 3:
        resultado = hashlib.sha256(string.encode())
        print('o hash da String :', string, 'é em SHA256: ', resultado.hexdigest())

    elif menu == 4:
        resultado = hashlib.sha512(string.encode())
        print('o hash da String :', string, 'é em SHA512: ', resultado.hexdigest())
    elif menu != '1234':
        print('\n***** OPÇÃO INVALIDA ***** digitou: ',menu)

print('\033[1;34mSaida do Sistema - obrigado e volte sempre !!')
exit()




#resultado = hashlib.md5(string.encode())



