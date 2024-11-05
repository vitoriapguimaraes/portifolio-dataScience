# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science
# => CAPÍTULO 14

### Análise estatística com o pacote Statsmodels em Linguagem Python ###

### Análise Estatística com Statsmodels ###

print("\n>>> Problema de Negócio: <<<")
print("""Existe alguma relação entre a área de imóveis (em metros quadrados)
e o valor do aluguel em uma determinada cidade?
Caso exista relação, como podemos mensurá-la?""")
print("\n")

# Imports
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm


# Carrega o dataset
df_dsa = pd.read_csv('Cap14/dataset.csv')

# Algumas informações
print(df_dsa.shape)
print("\n")

print(df_dsa.columns)
print("\n")

print(df_dsa.head())
print("\n")

print(df_dsa.info())
print("\n")

# Análise exploratória - resumo estatístico

# Verifica se há valores ausentes
print(df_dsa.isnull().sum())
print("\n")

# Resumo estatístico do dataset - ATENÇÃO => tem dado float, mas não faz sentido ver a média
print(df_dsa.describe())
print("\n")

# Resumo estatístico da variável alvo
print(df_dsa["valor_aluguel"].describe())
print("\n")

# Histograma da variável alvo
sns.histplot(data = df_dsa, x = "valor_aluguel", kde = True)
plt.show()

# Correlação entre as variáveis
print(df_dsa.corr())
print("\n")

# O coeficiente de correlação é uma medida estatística que indica a força e a
# direção da relação linear entre duas variáveis numéricas.
# Ele varia entre -1 e 1, onde:
#   Um coeficiente de correlação igual a 1 indica uma correlação linear perfeita
#     positiva, ou seja, quando uma variável aumenta, a outra variável também aumenta
#     na mesma proporção.
#   Um coeficiente de correlação igual a -1 indica uma correlação linear perfeita
#     negativa, ou seja, quando uma variável aumenta, a outra variável diminui na
#     mesma proporção.
#   Um coeficiente de correlação igual a 0 sugere que não há correlação linear
#     entre as duas variáveis.
#   O coeficiente de correlação mais comum é o de Pearson, que mede a correlação
#     linear entre duas variáveis. Existem outras medidas de correlação, como o
#     coeficiente de correlação de Spearman, que avalia a relação monotônica entre
#     duas variáveis, e o coeficiente de correlação de Kendall, que considera a
#     concordância entre os rankings das variáveis.

# Vamos analisar a relação entre a variável de entrada area_m2 e a variável alvo valor_aluguel
sns.scatterplot(data = df_dsa, x = "area_m2", y = "valor_aluguel")
plt.show()


### Regressão Linear Simples ###

# A Regressão Linear é uma técnica estatística utilizada para modelar a relação
# entre uma variável dependente (também chamada de variável resposta ou variável
# alvo) e uma ou mais variáveis independentes (também chamadas de variáveis
# explicativas ou preditoras). 
# 
# A Regressão Linear tem como objetivo estimar os coeficientes da equação que
# melhor descreve essa relação, minimizando a soma dos erros quadráticos entre
# os valores observados e os valores previstos pelo modelo.
# 
# Existem dois tipos principais de regressão linear:
#
#   => Regressão Linear Simples: Neste caso, há apenas uma variável independente
#     envolvida. A equação da Regressão Linear Simples é expressa como:
#     Y = a + bX + ε
#     Onde Y é a variável dependente, X é a variável independente, a é o
#     coeficiente linear (intercepto), b é o coeficiente angular (inclinação) e
#     ε é o erro aleatório.
#
#   => Regressão Linear Múltipla**: Neste caso, há duas ou mais variáveis
#     independentes envolvidas. A equação é expressa como:
#     Y = a + b1X1 + b2X2 + ... + bnXn + ε
#     Onde Y é a variável dependente, X1, X2, ..., Xn são as variáveis
#     independentes,a é o coeficiente linear (intercepto), b1, b2, ..., bn são
#     os coeficientes angulares (inclinações) e ε é o erro aleatório.
# 
# A Regressão Linear é amplamente utilizada em diversas áreas, como economia,
# ciências sociais, biologia e engenharia, para prever resultados, avaliar
# relações causais e identificar fatores que contribuem para um fenômeno específico.
# 
# Além disso, é uma técnica fundamental para a análise de dados e aprendizado de
# máquina, onde é usada para desenvolver modelos preditivos.


### Construção do Modelo OLS (Ordinary Least Squares) com Statsmodels em Python ###

print(df_dsa.head())

# Definimos a variável dependente
y = df_dsa["valor_aluguel"]

# Definimos a variável independente
X = df_dsa["area_m2"]

# O Statsmodels requer a adição de uma constante à variável independente
X = sm.add_constant(X)

# Criamos o modelo
modelo = sm.OLS(y, X)


# O método sm.OLS(y, X) é uma função do pacote Statsmodels, biblioteca Python
# utilizada para análise estatística. A função OLS (Ordinary Least Squares) é
# usada para ajustar um modelo de regressão linear, minimizando a soma dos erros
# quadráticos entre os valores observados e os valores previstos pelo modelo.
# 
# A função sm.OLS(y, X) recebe dois argumentos principais:
#   y: Um array ou pandas Series representando a variável dependente (variável
#     resposta ou alvo). É a variável que você deseja prever ou explicar com base
#     nas variáveis independentes.
#   X: Um array ou pandas DataFrame representando as variáveis independentes
#     (variáveis explicativas ou preditoras). São as variáveis que você deseja usar
#     para explicar ou prever a variável dependente.
#
# https://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.OLS.html

# Treinamento do modelo
resultado = modelo.fit()

print(resultado.summary())

### Interpretando o Resultado do Modelo Estatístico com Statsmodels ###

# A tabela acima traz um resumo do modelo com diversas estatísticas. Aqui faremos
# a análise de uma delas, o R².
# 
# O coeficiente de determinação, também conhecido como R², é uma medida estatística
# que avalia o quão bem o modelo de regressão se ajusta aos dados observados. Ele
# varia de 0 a 1 e representa a proporção da variação total da variável dependente
# que é explicada pelo modelo de regressão.
# 
# A interpretação do R² é a seguinte:
#   R² = 0: Neste caso, o modelo de regressão não explica nenhuma variação na
#     variável dependente. Isso significa que o modelo não é útil para prever ou
#     explicar a variável de interesse.
#   R² = 1: Neste caso, o modelo de regressão explica toda a variação na variável
#     dependente. Isso indica que o modelo se ajusta perfeitamente aos dados e é
#     extremamente útil para prever ou explicar a variável de interesse.
#   0 < R² < 1: Neste caso, o modelo de regressão explica uma parte da variação
#     na variável dependente. Quanto maior o valor de R², melhor o modelo se
#     ajusta aos dados e melhor é a sua capacidade de prever ou explicar a variável
#     de interesse.
# 
# É importante notar que um R² alto não garante que o modelo seja adequado, nem
# que haja uma relação causal entre as variáveis. Um R² alto pode ser resultado
# de variáveis irrelevantes, multicolinearidade ou até mesmo de um ajuste excessivo
# (overfitting). Portanto, é essencial avaliar outras estatísticas e diagnosticar
# o modelo antes de tirar conclusões definitivas.


# Plot
plt.figure(figsize = (12, 8))
plt.xlabel("area_m2", size = 16)
plt.ylabel("valor_aluguel", size = 16)
plt.plot(X["area_m2"], y, "o", label = "Dados Reais")
plt.plot(X["area_m2"], resultado.fittedvalues, "r-", label = "Linha de Regressão (Previsões do Modelo)")
plt.legend(loc = "best")
plt.show()


### Conclusão ###

# Claramente existe uma forte relação entre a área (em m2) dos imóveis e o valor
# do aluguel. Entretanto, apenas a área dos imóveis não é suficiente para explicar
# a variação no valor do aluguel, pois nosso modelo obteve um coeficiente de
# determinação (R²) de apenas 0.34.
# 
# O ideal seria usar mais variáveis de entrada para construir o modelo a fim de
# compreender se outros fatores influenciam no valor do aluguel.
# 
# É sempre importante deixar claro que correlação não implica causalidade e que
# não podemos afirmar que o valor do aluguel muda apenas devido à área dos imóveis.
# Para estudar causalidade devemos aplicar Análise Causal.
# 
# Em um Projeto de Regressão devemos validar as suposições (que são várias) antes
# de usar o modelo para tirar conclusões. 