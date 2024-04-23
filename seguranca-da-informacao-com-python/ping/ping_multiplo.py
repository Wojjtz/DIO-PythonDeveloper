import os
import time 

with open('projetos-seguranca_da_informacao/hosts.txt') as file: # abre o txt enquanto como arquivo
    dump = file.read() # variável para armazenar as linhas de conteúdo 
    dump = dump.splitlines()

    for ip in dump:
        print("Verificando o ip: ", ip)
        print("-" * 60)
        os.system(f'ping -n 2 {ip}')
        print("-" * 60)
        time.sleep(3) # tempo de espera para verificar o proximo ip