def exibir_mensagem():
    print("Hello World!")

def exibir_mensagem_2(nome):
    print(f"Seja bem vindo(a) {nome}!")

def exibir_mensagem_3(nome = "Anônimo"):
    print(f"Seja bem vindo (a) {nome}!")

exibir_mensagem()
exibir_mensagem_2(nome="Rodolfo")
exibir_mensagem_3()
exibir_mensagem_3(nome="Rodolfo")