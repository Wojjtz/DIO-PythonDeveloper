import socket # relaciomento da placa de rede com o SO
import sys # fornece acesso a algumas variaveis e funções do interpretador python

def main():
    # criando socket
    try:
        # objeto de conexão
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) # protocolo IP, tipo de protocolo, protocolo TCP 
    except socket.error as error:
        print("A conexão falhou!")
        print(f"Erro: {error}")
        sys.exit()

    print("Socket criado com sucesso!")

    # host e porta
    host_alvo = input("Digite o host ou IP a ser conectado: ")
    porta_alvo = input("Digite a porta a ser conectada: ")

    # fazendo a conexão do cliente com socket
    try:
        s.connect((host_alvo, int(porta_alvo)))
        print(f"Cliente TCP conectado com sucesso! \nHost: {host_alvo} \nPorta: {porta_alvo}")
        s.shutdown(2) # desconecta depois de 2 segundos
    except socket.error as error:
        print(f"Não foi possível conectar no Host: {host_alvo}, Porta: {porta_alvo}")
        print(f"Erro: {error}")
        sys.exit()

# chama a função main
if __name__ == "__main__":
    main()