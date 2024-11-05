# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science
# => CAPÍTULO 15

### Machine Learning com Scikit-Learn ###

print("\n>>> Problema de Negócio: <<<")
print("""Usando dados históricos é possível prever o salário de alguém com base
no tempo dedicado aos estudos em horas por mês?""")
print("\n")


# Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Carregando os dados

# Carrega o dataset
df_dsa = pd.read_csv('Cap15/dataset.csv')

print(df_dsa.shape)
print("\n")

print(df_dsa.columns)
print("\n")

print(df_dsa.head())
print("\n")

print(df_dsa.info())
print("\n")

# Análise Exploratória - Resumo Estatístico

# Verifica se há valores ausentes
print(df_dsa.isnull().sum())
print("\n")

# Correlação
print(df_dsa.corr())
print("\n")

# Resumo estatístico do dataset 
print(df_dsa.describe())
print("\n")

# Resumo estatístico da variável preditora
print(df_dsa["horas_estudo_mes"].describe())
print("\n")

# Histograma da variável preditora
sns.histplot(data = df_dsa, x = "horas_estudo_mes", kde = True)
plt.show()


### Preparação dos Dados ###

# Prepara a variável de entrada X
X = np.array(df_dsa['horas_estudo_mes'])

print(type(X))
print("\n")

# Ajusta o shape de X
X = X.reshape(-1, 1)

# Prepara a variável alvo
y = df_dsa['salario']

# Gráfico de dispersão entre X e y
plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.show()


# Dividir dados em treinamento e teste
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size = 0.2, random_state = 42)

print(X_treino.shape)
print(X_teste.shape)
print(y_treino.shape)
print(y_teste.shape)
print("\n")


### Modelagem Preditiva (Machine Learning) ###
# https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LinearRegression.html

# Cria o modelo de regressão linear simples
modelo = LinearRegression()

# Treina o modelo
modelo.fit(X_treino, y_treino)

# Visualiza a reta de regressão linear (previsões) e os dados reais usados no treinamento
plt.scatter(X, y, color = "blue", label = "Dados Reais Históricos")
plt.plot(X, modelo.predict(X), color = "red", label = "Reta de Regressão com as Previsões do Modelo")
plt.xlabel("Horas de Estudo")
plt.ylabel("Salário")
plt.legend()
plt.show()

# Avalia o modelo nos dados de teste
score = modelo.score(X_teste, y_teste)
print(f"Coeficiente R^2: {score:.2f}")
print("\n")


# Intercepto - parâmetro w0
print(modelo.intercept_)
print("\n")

# Slope - parâmetro w1
print(modelo.coef_)
print("\n")


### Deploy do Modelo ###

# Usaremos o modelo para prever o salário com base nas horas de estudo.

# Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[48]]) 

# Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print(f"Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)
print("\n")


# Mesmo resultado anterior usando os parâmetros (coeficientes) aprendidos pelo modelo
# y_novo = w0 + w1 * X
salario = modelo.intercept_ + (modelo.coef_ * horas_estudo_novo)
print(salario)
print("\n")


# Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[65]]) 

# Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print(f"Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)
print("\n")


# Define um novo valor para horas de estudo
horas_estudo_novo = np.array([[73]]) 

# Faz previsão com o modelo treinado
salario_previsto = modelo.predict(horas_estudo_novo)

print(f"Se você estudar cerca de", horas_estudo_novo, "horas por mês seu salário pode ser igual a", salario_previsto)
print("\n")