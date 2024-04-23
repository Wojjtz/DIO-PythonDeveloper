import hashlib

menu = """
Escolha o tipo de Hash
1 - md5
2 - sha1
3 - sha256
4 - sha512
0 - sair
R: """

while True:
    texto = input("Digite o texto a ser gerado o Hash: ")
    opcao = int(input(menu))
    if opcao == 1:
        result = hashlib.md5(texto.encode('utf-8'))
        print("Hash md5: ", result.hexdigest())
    elif opcao == 2:
        result = hashlib.sha1(texto.encode('utf-8'))
        print("Hash sha1: ", result.hexdigest())
    elif opcao == 3:
        result = hashlib.sha256(texto.encode('utf-8'))
        print("Hash sha256: ", result.hexdigest())
    elif opcao == 4:
        result = hashlib.sha512(texto.encode('utf-8'))
        print("Hash sha512: ", result.hexdigest())
    else:
        break