# Análise de Séries Temporais para Previsão de Vendas com Python e Suavização Exponencial
Este projeto aborda a análise e a previsão de vendas usando séries temporais. A partir dos dados históricos de vendas de 2023, ele visa prever o total de vendas para janeiro de 2024, utilizando técnicas de suavização exponencial com a biblioteca Statsmodels.
O principal objetivo é responder ao problema de negócio: "É possível prever o total de vendas em janeiro de 2024 a partir dos dados de vendas de 2023?"

## Tecnologias Utilizadas
- Python
- Bibliotecas:
   - Numpy, Pandas - para manipulação e análise de dados
   - Matplotlib, Seaborn - para visualização de dados
   - Statsmodels - para modelagem de séries temporais e suavização exponencial

## Funcionalidades
1. Pré-processamento de Dados: Carregamento e transformação da coluna de datas, conversão para uma série temporal.
   - Importação e Carregamento de Dados: Utilizando Pandas para manipular e exibir as características iniciais do dataset.
   - Transformação e Preparação dos Dados: Conversão da coluna de datas para o tipo datetime e definição do índice.
2. Análise Exploratória: Visualização das vendas ao longo do tempo e identificação de padrões sazonais e tendências.
   - Visualização Gráfica: Criação de gráficos de série temporal, com e sem formatação, para análise de tendências.
3. Construção e Treinamento do Modelo: Implementação da Suavização Exponencial Simples para prever vendas futuras.
4. Previsão de Vendas: Utilização do modelo treinado para prever o total de vendas em janeiro de 2024.
   - Deploy e Avaliação.

## Resultados
O modelo calcula a previsão das vendas para janeiro de 2024 com base nos dados históricos, oferecendo uma análise inicial de viabilidade.