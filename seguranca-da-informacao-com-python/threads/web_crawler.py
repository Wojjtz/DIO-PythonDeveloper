# web crawler é uma ferramenta usada para encontrar, ler e indexar páginas de um site
# muito utizilado em levantamento de informações em um processo de pentest
import requests
from bs4 import BeautifulSoup
import operator 
from collections import Counter

def start(url):
    # para armazenar o contéudo do site
    wordlist = []
    source_code = requests.get(url).text

    # requisição dos dados da url em html
    soup = BeautifulSoup(source_code, 'html.parser')

    # filtra tudo quer tiver 'div' e 'class'
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text

        # transforma em letras minuscuplas e divide o conteudo
        words = content.lower().split()

        for each_word in words:
            wordlist.append(each_word)
        
        clean_wordlist(wordlist)

# remove todos os simbolos indesejados da wordlist
def clean_wordlist(wordlist):
    clean_list = []
    
    for word in wordlist:
        symbols = '!@#$%¨&*()_-+={]}[|\;:"<>?/., '

        # substitui o simbolo encontrado por vazio
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)

    create_dictionary(clean_list)

# contagem das palavras e mostra as com mais ocorrências
def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else: 
            word_count[word] = 1

    # mostra quais palavras chave com mais ocorrência
    for key, value in sorted(word_count.items(), key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)

    top = c.most_common(10)

    print(top)

if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=gcse")