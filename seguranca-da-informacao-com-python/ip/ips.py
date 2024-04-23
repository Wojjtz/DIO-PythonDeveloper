import ipaddress

ip = "192.168.0.1"

# transforma em ip
endereco = ipaddress.ip_address(ip)

print(endereco)
print(endereco + 100)
print(endereco + 257)
print(endereco + 2000)

# com rede

ip_rede = "192.168.0.0/24"

rede = ipaddress.ip_network(ip_rede, strict=False) # 'strict = False' habilita a possibilidade de inserção de qualquer ip, mesmo não sendo de rede

print(rede)

# imprimindo todos os ip da rede
for ip in rede:
    print(ip)