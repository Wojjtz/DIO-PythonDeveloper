class Bicicleta:
    # self == this do Java
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo 
        self.ano = ano 
        self.valor = valor 
    
    def buzinar(self):
        print("Plim Plim...")

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def  acelerar(self):
        print("Vrummmmm!!!")

#   def __str__(self):
#       return f"Bicicleta: cor = {self.cor}, modelo = {self.modelo}, ano = {self.ano}, valor = {self.valor}"

    def __str__(self):
        return f"{self.__class__.__name__} : {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

b = Bicicleta("marrom", "caloi", 1997, 500)
b.acelerar()
b.buzinar()
b.parar()
print(b.cor, b.modelo, b.ano, b.valor)

b2 = Bicicleta("verde", "monark", 2000, 189)
# retorna valor de memória 
print(b2)
b2.acelerar()

Bicicleta.buzinar(b)
Bicicleta.buzinar(b2)

print(b)