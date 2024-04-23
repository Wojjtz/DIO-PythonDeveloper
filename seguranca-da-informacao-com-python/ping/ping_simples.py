import os # integra os programas e recursos do SO

print("#" * 60)
ip_ou_host = input("Digite o IP ou Host a ser verificado: ")
print("-" * 60)

# comando de sistemas
os.system(f'ping -n 6 {ip_ou_host}') # verificado a conexão com determinado ip ou host
print("-" * 60)