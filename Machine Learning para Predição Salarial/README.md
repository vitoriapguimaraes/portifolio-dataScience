# Predição Salarial com Machine Learning Baseada em Horas de Estudo

Este projeto tem como objetivo prever o salário com base na quantidade de horas dedicadas aos estudos por mês, utilizando dados históricos. A análise explora se há uma relação linear entre as horas de estudo e o salário mensal.

## Tecnologias Utilizadas
- Python
- Bibliotecas: Scikit-Learn, NumPy, Pandas, Matplotlib, Seaborn

## Etapas do Projeto
1. Análise Exploratória dos Dados
   - Carregamento e inspeção do conjunto de dados.
   - Análise de correlação e distribuição das variáveis.
2. Pré-processamento
   - Separação dos dados em variáveis independentes (horas de estudo) e dependentes (salário).
   - Divisão dos dados em conjunto de treino e teste para avaliação do modelo.
3. Modelagem Preditiva
   - Construção e treinamento do modelo de Regressão Linear Simples.
   - Visualização dos dados históricos e da reta de regressão do modelo.
4. Avaliação do Modelo
   - Avaliação do coeficiente **R&sup2;** para medir o desempenho do modelo nos dados de teste.
5. Previsões
   - Utilização do modelo para prever salários com base em novos valores de horas de estudo.

## Resultados e Conclusões
A relação entre as horas de estudo e o salário é representada pelo coeficiente **R&sup2;**, indicando a precisão do modelo na predição salarial. Previsões foram feitas para diferentes valores de horas de estudo, proporcionando insights sobre a influência da dedicação nos estudos sobre a remuneração esperada.