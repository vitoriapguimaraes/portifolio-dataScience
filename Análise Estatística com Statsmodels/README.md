# Análise de Regressão Linear para Predição do Valor de Aluguel de Imóveis com Statsmodels
Este projeto visa investigar a relação entre a área de imóveis (em metros quadrados) e o valor do aluguel em uma determinada cidade, aplicando técnicas de Regressão Linear Simples com a biblioteca Statsmodels em Python. Através deste modelo, buscamos responder se existe uma relação significativa entre essas variáveis e, caso exista, como podemos quantificar essa relação.

## Objetivo
O objetivo deste projeto é construir um modelo de regressão linear que possa prever o valor do aluguel de imóveis com base em sua área em metros quadrados. O modelo será avaliado pelo coeficiente de determinação **R&sup2;**, entre outras métricas estatísticas.

## Bibliotecas Utilizadas
- pandas para manipulação de dados
- matplotlib e seaborn para visualização de dados
- statsmodels para a modelagem estatística de Regressão Linear

## Estrutura do Projeto
1. Análise Exploratória dos Dados:
    - Visualização da distribuição do valor do aluguel.
    - Análise de correlação entre as variáveis <code>area_m2</code> e <code>valor_aluguel</code>.
2. Modelagem Estatística:
    - Construção de um modelo de Regressão Linear Simples (OLS - Ordinary Least Squares) para prever <code>valor_aluguel</code> com base na <code>area_m2</code>.
    - Exibição dos coeficientes do modelo e interpretação do **R&sup2;**.
3. Visualização dos Resultados:
    - Plotagem da linha de regressão sobre os dados reais para visualização da adequação do modelo.
4. Conclusão:
    - Análise do resultado obtido e sugestões para melhorar o modelo, como adicionar mais variáveis explicativas.

## Interpretação dos Resultados
O modelo de Regressão Linear apresentou um coeficiente de determinação **R&sup2;** que indica a fração da variabilidade de <code>valor_aluguel</code> explicada por <code>area_m2</code>. No entanto, um valor baixo de **R&sup2;** sugere que apenas a área do imóvel pode não ser suficiente para prever o valor do aluguel com precisão. Outras variáveis podem ser consideradas para melhorar o modelo.

## Considerações
- Este projeto tem caráter exploratório e não visa estabelecer causalidade.
- É recomendado utilizar mais variáveis e validar as suposições do modelo de regressão antes de utilizá-lo para fins de tomada de decisão.
