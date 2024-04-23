import random, string

tamanho = 16 # tamanho recomendado para senhas fortes

# recebe a estrutura da senha a ser gerada
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+;:/?ç' # letras maiusculas e minusculas / numeros de 0 a 9 / caracteres

# SystemRandom utiliza a biblioteca 'os.urandom', que gera numeros aleatorios fornecidos pelo SO
rnd = random.SystemRandom()

# concatena os de caracteres aleatorios
print(''.join(rnd.choice(chars) for i in range(tamanho)))