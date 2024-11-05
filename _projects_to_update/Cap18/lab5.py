# CURSO: Fundamentos de Linguagem Python para Analise de Dados e Data Science
# => CAPÍTULO 18

### LAB 5
# Robô Trading com Inteligência Artificial em Linguagem Python

# Neste Lab trabalharemos com dados reais disponíveis publicamente no link abaixo:
# https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv

# Nosso objetivo é criar um sistema de IA que aprenda a operar na bolsa de
# valores e # seja capaz de, a partir de um saldo inicial, tomar decisões de
# compra e venda de ações visando obter lucro.

### Problema de Negócio: ###

# Construir um robô (modelo em Linguagem Python) baseado em Inteligência Artificial
# que aprenda a operar na bolsa de valores a partir de experimentos de compra e
# venda de ações. Dado um saldo inicial o modelo deve apresentar o resultado
# (lucro) a ser obtido depois de ações de compra e venda.

# Imports
import random
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from datetime import datetime

# Carregando e Visualizando os Dados com Candlestick

# Carrega os dados
df = pd.read_csv('Cap18/dataset.csv')

print("Dataset Shape:", df.shape)

print("\nPrimeiras 5 Linhas:")
print(df.head())

# O Candlestick é um tipo de gráfico financeiro utilizado para descrever a
# movimentação de preços de determinados ativos (ações, criptomoedas, etc.). Em
# contraste com um gráfico de linha simples do preço de fechamento, ele oferece
# muito mais informações sobre a dinâmica dos preços - é baseado em dados OHLC,
# o que significa que contém os preços de abertura, alta, baixa e fechamento
# (geralmente junto com o volume). Esses valores podem ser mostrados em diferentes
# frequências de amostragem (minuto, hora, dia, semana, etc.) e são frequentemente
# usados como base para análises técnicas.
# https://plotly.com/python/candlestick-charts/

# Candlestick
fig = go.Figure(data = [go.Candlestick(x = df['Date'],
                open = df['AAPL.Open'],
                high = df['AAPL.High'],
                low = df['AAPL.Low'],
                close = df['AAPL.Close'])])
fig.show()

# Vamos trabalhar com a cotação de fechamento da ação da Apple
precos = df['AAPL.Close'].values

print("Tipo dos Preços:", type(precos))

print(f"-"*50)

# Configuração do Algoritmo Q-Learning

# Configuração do Q-Learning
print('\nDefinindo os Hiperparâmetros do Q-Learning...')
num_episodios = 1000
alfa = 0.1
gama = 0.99
epsilon = 0.1

# Configuração do ambiente de negociação
print('\nConfigurando o Ambiente de Negociação...')
acoes = ['comprar', 'vender', 'manter']
saldo_inicial = 1000
num_acoes_inicial = 0

# Função Para Executar as Ações (Passos) do Robô Trading
# Função para executar uma ação e retornar a recompensa e o próximo estado
def executar_acao(estado, acao, saldo, num_acoes, preco):
    
  # Ação de comprar
  if acao == 0:  
    if saldo >= preco:
      num_acoes += 1
      saldo -= preco
    
  # Ação de vender
  elif acao == 1:  
    if num_acoes > 0:
      num_acoes -= 1
      saldo += preco

  # Define o lucro
  lucro = saldo + num_acoes * preco - saldo_inicial

  return (saldo, num_acoes, lucro)

# Treinamento do Robô

# Inicializar a tabela Q
print('\nInicializando a Tabela Q...')
q_tabela = np.zeros((len(precos), len(acoes)))

# Treinamento
print('\nInicializando o Treinamento...')
for _ in range(num_episodios):
    
  # Define o saldo
  saldo = saldo_inicial
    
  # Define o número de ações
  num_acoes = num_acoes_inicial

  # Loop
  for i, preco in enumerate(precos[:-1]):
        
    estado = i

    # Escolher a ação usando a política epsilon-greedy
    if np.random.random() < epsilon:
      acao = random.choice(range(len(acoes)))
    else:
      acao = np.argmax(q_tabela[estado])

    # Executar a ação e obter a recompensa e o próximo estado
    saldo, num_acoes, lucro = executar_acao(estado, acao, saldo, num_acoes, preco)
    prox_estado = i + 1

    # Atualizar a tabela Q
    q_tabela[estado][acao] += alfa * (lucro + gama * np.max(q_tabela[prox_estado]) - q_tabela[estado][acao])

print('\nTreinamento Concluído...')

# Executando o Robô Trading e Prevendo o Lucro de Operações na Bolsa de Valores

# Valores iniciais para testar o agente
saldo = saldo_inicial
num_acoes = num_acoes_inicial

print('\nExecutando o Agente...')
for i, preco in enumerate(precos[:-1]):
    estado = i
    acao = np.argmax(q_tabela[estado])
    saldo, num_acoes, _ = executar_acao(estado, acao, saldo, num_acoes, preco)
    
print('\nExecução Concluída...')

print("\nQuantidade de Ações Compradas:", num_acoes)

print ("O último valor de venda: R$", precos[-1])

# Vendendo todas as ações no último preço
saldo += num_acoes * precos[-1]
lucro = saldo - saldo_inicial
lucro_final = round(lucro,2)

print(f"\nComeçamos a Negociação com Saldo Inicial de R$ 1000 e tivemos Lucro de: R$ {lucro_final:.2f} .")

print("\nObrigado Por Usar o Robô Trading do Curso Gratuito da DSA.\n")