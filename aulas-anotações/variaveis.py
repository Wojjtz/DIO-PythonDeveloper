print(11 + 10 + 1000)
print(1.5 + 1 + 0.5)
print(True)
print(False)
print("Python")

#declaração de variaveis
idade = 19
nome = 'Rodolfo'
print(f'Meu nome é {nome} e tenho {idade} anos.')

idade, nome = (21, 'Eduardo')
print(f'Meu nome é {nome} e tenho {idade} anos.')

#constante: declarar com todas a letras maiusculas 
ABS_PATH = '/home/rodolfo/Docs/python_course'
DEBUG = True
STATES = [ 'SP', 'MG', 'RJ']
AMOUNT = 54

#declaração de variaveis: snake_case
limite_de_saque_diario = 1000

BRAZILIAN_STATES = ["SP", "RJ", "MG", "RS"]

#conversão de variaveis
preco = 10 #10
preco = float(preco) #10.0

preco = 10.30 #10.3
preco = int(preco) #10

#conversão por divisão
preco = 10
print(preco / 2) #5.0
print(preco // 2) #5 (// retorna inteiro)

preco = 10.50
idade = 28
print(str(preco))
print(str(idade))
texto = f"idade {idade} e preço {preco}" #idade 28 e preco 10.50 (f: formatar texto com variaveis)

preco = "10.50"
idade = "28"
print(float(preco)) #10.50
print(float(idade)) #28

#erro de conversão
preco = "python"
print(float(preco))

#type() retorna o tipo da variavel
print(type(str(10.10))) #retorna 'str'
