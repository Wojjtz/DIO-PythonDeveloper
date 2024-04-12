class Cachorro:
    # classe "construtora" (inicializadora)
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    # classe destrutora (python já possui coletor de lixo, não é preciso declarar a classe 'del')
    # implementado mais para gerar uma ação ANTES de deletar um objeto
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

del c

# criar_cachorro()