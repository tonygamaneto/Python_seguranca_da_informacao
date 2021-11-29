from threading import  Thread
from time import sleep

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <=100:
        print('Piloto: {}  Km: {} \n'.format(piloto, trajeto))
        trajeto += velocidade
        sleep(1)

t_carro1 =Thread(target=carro, args=[1, 'Bruno'])
t_carro2 =Thread(target=carro, args=[2, 'Natan'])

t_carro1.start()
t_carro2.start()

carro(1)