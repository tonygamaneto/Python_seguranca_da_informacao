import hashlib

arquivo1 = 'a.txt'
arquivo2 = 'b.txt'

hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'\033[1;31mO ARQUIVO: {arquivo1} hash: {hash1.hexdigest()} É DIFERENTE DO ARQUIVO: \033[1;32m{arquivo2} hash {hash2.hexdigest()}\033[1;m')
else:
    print(f'\033[1;34mO ARQUIVO: {arquivo1} HASH: {hash1.hexdigest()} É IGUAL AO ARQUIVO:\033[1;33m {arquivo2} HASH: {hash2.hexdigest()}\033[1;m')

