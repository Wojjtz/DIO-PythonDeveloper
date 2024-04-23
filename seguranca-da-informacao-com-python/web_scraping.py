# web scraper é uma ferramenta de coleta de dados web
# mineração que permite a extração de dados de sites da web convertentdo-os em informação estruturada para posterior análise
from bs4 import BeautifulSoup
import requests

# objeto site recebendo o conteudo da requisição https do site
site = requests.get("https://www.climatempo.com.br/").content

# objeto soup baixando o site em html
soup = BeautifulSoup(site, 'html.parser')

# transforma html em string
print(soup.prettify())

# é possível encontrar um valor ou palavra utilizando o método .find
# soup.find(valores do campo a se encontrar)