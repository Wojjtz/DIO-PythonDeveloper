texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

print()

#range: produz uma sequência de numeros inteiras a partir de um inicio e para um fim
#range(stop) -> range object
#range(start, stop[, step]) -> range object
list(range(4))

for numero in range(0,11):
    print(numero, end=", ")

#exibindo tabuada do 5
for numero in range(0, 51, 5):
    print(numero, end=", ")

#while
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")

#while/else
opcao = -1
while opcao != 0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))

    if opcao == 1:
        print("Sacando...")
    elif opcao == 2:
        print("Exibindo extrato...")
else:
    print("Obrigado por usar nosso sistema bancário, até logo!")

