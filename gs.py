import random
import string

tamanho = int(input('qual o tamanho de sua senha: '))
chars = string.ascii_letters + string.digits + 'çÇ!@#$%¨&*()_-+={}[]~^^?/;:.,'
rnd = random.SystemRandom() #os.urandom

print(''.join(rnd.choice(chars)for i in range(tamanho)))
