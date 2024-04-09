# Somente por posição

# antes da / = somento por posição 
# depois da / = por posicao ou keyword (chave)

def criar_carro(modelo, ano, placa, /, marca, motor, combustivel): 
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# Somente por keyword

# depois do * = somente por keyword 

def criar_carro_2(*, modelo, ano, placa, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_2(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro_2("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # inválido


# Hibrido // posicão e keyword

def criar_carro_3(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro_3("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") # válido

criar_carro_3(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido