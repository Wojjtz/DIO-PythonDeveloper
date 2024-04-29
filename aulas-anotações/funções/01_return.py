def calcular_total(numeros):
    return sum(numeros)

def antecessor_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor # retorna em um tupla

# funções sem return explicito retornan "None"

print(calcular_total([10,20,34])) # 64
print(antecessor_sucessor(10)) # (9,11)