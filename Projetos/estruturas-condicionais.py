MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")

if idade < MAIOR_IDADE:
    print("Menor de idade, não pode tirar CNH")

#if else
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
else:
    print("Menor de idade, não pode tirar CNH")

#if elif else (elif = else if do java)
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
elif idade >= IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não aulas práticas")
else:
    print("Menor de idade, não pode tirar CNH")


#if ternário
saldo = 100
saque = 20

status = "Sucesso" if saldo >= saque else "Falha"
print(f"{status} ao realizar o saque!")