#operadores aritmeticos são iguais ao Java
# // divisão inteira, sem considerar resto

#lógicos
saldo = 1000
saque = 200
limite = 100
conta_especial = True

saldo >= limite #true
saque <= limite #false

saldo >= saque and saque <= limite #false
saldo >= saque or saque <= limite #true

contatos_emergencia = []

not 1000 > 1500 #true

not contatos_emergencia #true

saldo >= saque and saque <= limite or conta_especial and saldo >= saque #true
(saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque) #true

#identidade
curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

curso is nome_curso #True

curso is not nome_curso #False

saldo is limite #True

#associação
curso = "Curso de Python"
frutas = ["laranja", "uva", "limão"]
saques = [1500, 100]

"Python" in curso #True

"maçã" not in frutas #True

200 in saques #False

