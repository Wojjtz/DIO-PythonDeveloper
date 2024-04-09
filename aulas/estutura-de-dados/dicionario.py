# Dicionário é um conjunto não-ordenado de pares chave: valor, onde as chaves são únicas em um dada instância do dic.

pessoa = {"nome": "Rodolfo", "idade": 19}

pessoa = dict(nome="Rodolfo", idade=19)

pessoa["telefone"] = "2222-1234" # {"nome" : "Rodolfo", "idade" : 19, "telefone" : "2222-1234"} // adicionando chave em um dic existente

# Acesso

dados = {"nome" : "Rodolfo", "idade" : 19, "telefone" : "2222-1234"}
print(dados["nome"])
print(dados["idade"])
print(dados["telefone"])

dados["nome"] = "João"
dados["idade"] = "21"
dados["telefone"] = "1111-1234"

print(dados)

# Dicionáriso Aninhados

contatos = {
    "guilherme@gmail.com" : {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

# Iteração

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items(): # não é a melhor forma de iterar
    print(chave, valor)

# Métodos da Classe "dict"

# Clear

contatos.clear()
print(contatos)

# Copy

contatos = {"rodolfo@gmail.com": {"nome": "Rodolfo", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["rodolfo@gmail.com"] = {"nome": "Rod"}

print(contatos["rodolfo@gmail.com"])  # {"nome": "Rodolfo", "telefone": "3333-2221"}

print(copia["rodolfo@gmail.com"])  # {"nome": "Rod"}

# Fromkeys // "cria" chaves no dicionário

resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"} // adiciona algum valor já pré-definido
print(resultado)

# Get

contatos = {"rodolfo@gmail.com": {"nome": "Rodolfo", "telefone": "3333-2221"}}

#contatos["chave"]  # KeyError // chave não existe

resultado = contatos.get("chave")  
print(resultado) # None
resultado = contatos.get("chave", {}) 
print(resultado) # {} // valor "default"

resultado = contatos.get("guilherme@gmail.com", {})  
print(resultado) # {"rodolfo@gmail.com": {"nome": "Rodolfo", "telefone": "3333-2221"}

# Items // retorna lista de tuplas

resultado = contatos.items()  # dict_items([('rodolfo@gmail.com', {'nome': 'Rodolfo', 'telefone': '3333-2221'})])
print(resultado)

# Keys // retorna as chaves do dicionário, não os valores

resultado = contatos.keys()  # dict_keys(['rodolfo@gmail.com'])
print(resultado)

# Pop // remove uma chave do dicionário

resultado = contatos.pop("rodolfo@gmail.com")  # {'nome': 'Rodolfo', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("rodolfo@gmail.com", {})  # {}
print(resultado)

# PopItem

contatos = {"rodolfo@gmail.com": {"nome": "Rodolfo", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('rodolfo@gmail.com', {'nome': 'Rodolfo', 'telefone': '3333-2221'})
print(resultado)

#contatos.popitem()  # KeyError

# SetDefault

contato = {"rodolfo@gmail.com": {"nome": "Rodolfo", "telefone": "3333-2221"}}

contato.setdefault("nome", "Giovanna")  # "Rodolfo" // se o atributo existe, ele não subsitui o original 
print(contato)  # {'nome': 'Rodolfo', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Rodolfo', 'telefone': '3333-2221', 'idade': 28}

# Update

contatos = {"rodolfo@gmail.com": {"nome": "Rodolfo", "telefone": "3333-2221"}}

contatos.update({"rodolfo@gmail.com": {"nome": "Rod"}}) # {'rodolfo@gmail.com': {'nome': 'Rod'}}
print(contatos) 

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}}) # {'rodolfo@gmail.com': {'nome': 'Rod'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}

print(contatos)

# Values

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'Guilherme', 'telefone': '3333-2221'}, {'nome': 'Giovanna', 'telefone': '3443-2121'}, {'nome': 'Chappie', 'telefone': '3344-9871'}, {'nome': 'Melaine', 'telefone': '3333-7766'}])  # noqa
print(resultado)

# In

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

resultado = "guilherme@gmail.com" in contatos  # True
print(resultado)

resultado = "megui@gmail.com" in contatos  # False
print(resultado)

resultado = "idade" in contatos["guilherme@gmail.com"]  # False
print(resultado)

resultado = "telefone" in contatos["giovanna@gmail.com"]  # True
print(resultado)

# Del

contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

del contatos["guilherme@gmail.com"]["telefone"]
del contatos["chappie@gmail.com"]

# {'guilherme@gmail.com': {'nome': 'Guilherme'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3443-2121'}, 'melaine@gmail.com': {'nome': 'Melaine', 'telefone': '3333-7766'}}  # noqa
print(contatos)