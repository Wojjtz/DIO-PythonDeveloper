import json
from urllib.request import urlopen

url = 'https://ipinfo.io/json'

resposta = urlopen(url)

dados = json.load(resposta)

ip = dados['ip']
org = dados['org']
cidade = dados['city']
pais = dados['country']
regiao = dados['region']

print(f'Detalhes da URL: \nIP: {ip} \nRegião: {regiao} \nCidade: {cidade} \nPaís: {pais} \nOrganização: {org}')