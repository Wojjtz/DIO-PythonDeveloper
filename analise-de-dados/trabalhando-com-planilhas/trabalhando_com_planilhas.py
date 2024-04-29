import pandas as pd

df1 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Aracaju.xlsx')
df2 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Fortaleza.xlsx')
df3 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Natal.xlsx')
df4 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Recife.xlsx')
df5 = pd.read_excel('analise-de-dados/trabalhando-com-planilhas/planilhas/Salvador.xlsx')

print(df2.head())

df = pd.concat([df1,df2,df3,df4,df5])

print(df.head())

print(df.tail())

# Retorna amostras, aleatórias
print(df.sample(5))

print(df.dtypes)

# Altera o tipo de dado da coluna
df["LojaID"] = df["LojaID"].astype("object")

# Consultando linhas com valores faltantes
print(df.isnull().sum())

# Substituindo os valores nulas pela média
# df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# Substituindo os valores nulas por 0
# df["Vendas"].fillna(0, inplace=True)

# Apagando as linhas com valores nulos
df.dropna(inplace=True)

# Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

# Criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])

df["Receita/Vendas"] = df["Receita"] / df["Vendas"] 

# Max/Min
df["Receita"].max()
df["Receita"].min()

# nlargest // 3 linhas com maiores receitas
df.nlargest(3, "Receita")

# nsamllest // 3 linhas com menores receitas
df.nsmallest(3, "Receita")

# Agrupamento por cidade
df.groupby("Cidade")["Receita"].sum()

# Ordenando o conjunto de dados
df.sort_values("Receita", ascending=False).head(10)

# Transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

# Transformando coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])

# Agrupamento por ano
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

# Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year

print(df.sample(5))

# Extraindo o mês e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

# Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter
print(df.sample(5))

# Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]
print(vendas_marco_19.sample(20))