#maiúscula, minúscula e título
curso = "pytHon"

print(curso.upper()) #PYTHON

print(curso.lower()) #python

print(curso.title()) #Python

#eliminando espaços em branco
curso = "   Python "

print(curso.strip()) #"Python"

print(curso.lstrip) #"Python " 

print(curso.rstrip) #"   Python"   

#junções e centralização
curso = "Python"

print(curso.center(10,"#")) #"##Python##" (numero de casas, texto à inserir)
print(curso.center(10))#"  Python  "

print(".".join(curso))#"P.y.t.h.o.n"

#interpolação
nome = "Rodolfo"
idade = 19
profissao = "Dev"
linguagem = "Python"

#old style
print("Olá, me chamo %s. Tenho %d anos de idade, trabalho como %s e programo em %s." % (nome, idade, profissao, linguagem))

#f-string
print(f"Olá me chamo {nome}. Tenho {idade} anos de idade, trabalho como {profissao} e programo em {linguagem}")

#formatar com f-string
PI = 3.14159
print(f"Valor de PI: {PI:.2f}")#"Valor de PI: 3.14"
print(f"Valor de PI: {PI:10.2f}")#"Valor de PI:           3.14"

#fatiamento
nome = "Rodolfo Oliveira Miranda"

print(nome[0]) #R
print(nome[:7]) #Rodolfo
print(nome[8:]) #Oliveira Miranda
print(nome[8:16]) #Oliveira 
print(nome[8:16:2]) #Oier
print(nome[:]) #Rodolfo Oliveira Miranda
print(nome[::-1]) #adnariM arievilO oflodoR

#string múltiplas linhas
nome = "Rodolfo"

mensagem = f"""
Olá meu nome é {nome},
Eu estou aprendendo Python
"""

print(mensagem)

mensagem = f'''
        Olá meu nome é {nome},
    Eu estou aprendendo Python
'''

print(mensagem)

print("""
================== MENU ====================
      
    1 - Depositar
    2 - Sacar
    0 - Sair

    Obrigado por usar nosso sistema!!!

============================================
""")










