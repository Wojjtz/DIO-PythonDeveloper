import hashlib

arquivo_1 = 'seguranca-da-informacao-com-python/comparador-de-hashes/arquivo-1.txt'
arquivo_2 = 'seguranca-da-informacao-com-python/comparador-de-hashes/arquivo-2.txt'
# arquivo_2 = 'seguranca-da-informacao-com-python/comparador-de-hashes/arquivo-1-copia.txt'

# indica qual algoritmo hash que será usado
hash_1 = hashlib.new('ripemd160')

# indica qual arquivo será comparado
hash_1.update(open(arquivo_1, 'rb').read()) # open(arquivo_1) abre o arquivo, rb é um método de leitura em binário

# criando segundo hash para o segundo arquivo
hash_2 = hashlib.new('ripemd160')
hash_2.update(open(arquivo_2, 'rb').read())

# comparação 
if hash_1.digest() != hash_2.digest(): # .digest() resume os dados passados pelo update
    print(f"""
Arquivos Diferentes!
Hash {arquivo_1}: {hash_1.hexdigest()}
Hash {arquivo_2}: {hash_2.hexdigest()}
""")
    
else:
    print(f"""
Arquivos Iguais!
Hash {arquivo_1}: {hash_1.hexdigest()}
Hash {arquivo_2}: {hash_2.hexdigest()}
""")