import pandas as pd

df = pd.read_csv("analise-de-dados/trabalhando-com-planilhas/planilhas/Gapminder.csv", sep=";", on_bad_lines='skip', encoding='unicode_escape')

# Visualizando as 5 primeiras linhas
print(df.head())

# altera o nome das colunas
df = df.rename(columns={"country":"Pais", "continent": "continente", "year":"Ano", "lifeExp":"Expectativa de vida", "pop":"Pop Total", "gdpPercap": "PIB"})
    
print(df.head(10))

# Total de linhas e colunas
print(df.shape)

print(df.columns)

# Retorna o tipo dos dados de cada coluna
df.dtypes

df.tail(15)

# Retorna informações e estatísticas 
df.describe()

# Localizar de acordo com atributo
df["continente"].unique()

Oceania = df.loc[df["continente"] == "Oceania"]
print(Oceania.head())

# Retorna quantos paises existem para cada continente
print(df.groupby("continente")["Pais"].nunique())

# Retorna qual a expecativa de vida média para cada ano
print(df.groupby("Ano")["Expectativa de vida"].mean())

# Média PIB
df["PIB"].mean()

# Soma PIB
df["PIB"].sum()