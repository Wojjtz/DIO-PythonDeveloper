# utilizando uma thread

def carro_1 (velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Carro 1: ', trajeto)
        trajeto += velocidade

def carro_2 (velocidade):
    trajeto = 0
    while trajeto <= 100:
        print('Carro 2: ', trajeto)
        trajeto += velocidade

carro_1(10)
carro_2(20)