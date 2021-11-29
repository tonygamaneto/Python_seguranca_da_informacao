import  ipaddress

ip = '192.168.0.0/0'
rede= ipaddress.ip_network(ip, strict=False)


#endereco = ipaddress.ip_address(ip)

for ip in rede:
    print(ip)
