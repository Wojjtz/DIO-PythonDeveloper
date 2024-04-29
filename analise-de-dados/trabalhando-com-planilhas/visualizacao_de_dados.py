# rodar com Jupyter
# barra de pesquisa -> ">Jupyter Notebook"
import pandas as pd

df1 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Aracaju.xlsx')
df2 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Fortaleza.xlsx')
df3 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Natal.xlsx')
df4 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Recife.xlsx')
df5 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Salvador.xlsx')

df = pd.concat([df1,df2,df3,df4,df5])
df["LojaID"].value_counts(ascending=False)

# Gráfico de barras
df["LojaID"].value_counts(ascending=False).plot.bar()