frutas = ["laranja", "maça", "uva"]

frutas = []

letras = list("python") # p, y, t, h, o, n

numeros = list(range(10)) # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
 
carro = ["Ferrari", "F8", 4200000, 2020, 2900, "São Paulo", True]

# Acesso
frutas = ["maçã", "laranja", "uva", "pera"]
frutas[0] # maçã
frutas[2] # uva

frutas[-1] # pera
frutas[-3] # laranja

# Matrizes
matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

# Fatiamento 
lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

# Função Enumerate
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Compreensão de Listas
# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        # pares = [numero for numero in numeros if numero % 2 == 0] // inline
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []
for numero in numeros:
    quadrado.append(numero**2)
    # quadrado = [numero**2 for numero in numeros] // inline
print(quadrado)

# Métodos da Classe List
# Adicionar
lista = [] 

lista.append(1)
lista.append("Python")
lista.append([40,30,20])

print(lista)

# Limpar
lista.clear()

l2 = print(lista)  # []

# Copy // (retorna uma nova instância da lista desejada, não a original)
lista.copy()
print(id(l2), id(lista)) 

# Count
cores = ["vermelho", "azul", "verde", "azul"]

print(cores.count("vermelho"))  # 1
print(cores.count("azul"))  # 2
print(cores.count("verde"))  # 1

# Extend
linguagens = ["python", "js", "c"]

print(linguagens)  # ["python", "js", "c"]

linguagens.extend(["java", "csharp"]) # não remove valores duplicados

print(linguagens)  # ["python", "js", "c", "java", "csharp"]

# Index
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

# Pop (lista pode comporta-se como pilha)
linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp // (ultimo elemento adicionado)
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

# Remove
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.remove("c") # remove apenas a primeira ocorrência de 'c'

print(linguagens)  # ["python", "js", "java", "csharp"] 

# Reverse
linguagens = ["python", "js", "c", "java", "csharp"]

linguagens.reverse()

print(linguagens)  # ["csharp", "java", "c", "js", "python"]

# Sort
linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort()  # ["c", "csharp", "java", "js", "python"] // ordena de forma alfabética 
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(reverse=True)  # ["python", "js", "java", "csharp", "c"] // ordena ou espelha
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x))  # ["c", "js", "java", "python", "csharp"] // ordena por tamanho da palavra (crescente)
print(linguagens)

linguagens = ["python", "js", "c", "java", "csharp"]
linguagens.sort(key=lambda x: len(x), reverse=True)  # ["python", "csharp", "java", "js", "c"] // ordena por tamanho da palavra (decrescente)
print(linguagens)

# Len // retorna o tamanho da lista
linguagens = ["python", "js", "c", "java", "csharp"]

print(len(linguagens))  # 5

# Sorted
linguagens = ["python", "js", "c", "java", "csharp"]

print(sorted(linguagens)) # ordem alfabética
print(sorted(linguagens, key=lambda x: len(x)))  # ["c", "js", "java", "python", "csharp"]
print(sorted(linguagens, key=lambda x: len(x), reverse=True))  # ["python", "csharp", "java", "js", "c"]