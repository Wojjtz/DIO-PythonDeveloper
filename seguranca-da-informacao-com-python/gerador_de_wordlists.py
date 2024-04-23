# wordlists são arquivos contendo uma palavra por linha
# utilizadas em ataques de força bruta, como quebra de autenticação
# também para testar a autenticação e confidencialidade de um sistema
import itertools

string = input("String a ser permutada: ")

# permutação das palavras, caracteres
result = itertools.permutations(string, len(string)) # caracteres, quantidade de caracter por permutação

for i in result:
    print(''.join(i))