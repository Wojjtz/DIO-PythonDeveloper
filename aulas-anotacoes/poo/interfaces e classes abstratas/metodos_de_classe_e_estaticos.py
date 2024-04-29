# método de classe: ligados à classe e não ao objeto. recebe argumento que aponta para a classe
# método estatico: não recebe argumento explícito

# utilizar método de classe para criar métodos de fábrica (método que retornam instâncias daquela classe)
# utilizar método estático para criar funções utilitárias

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # cls: metodo da classe
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18


p = Pessoa.criar_de_data_nascimento(2005, 2, 17, "Rodolfo")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))