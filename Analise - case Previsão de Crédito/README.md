# Sistema de Previsão de Score de Crédito para Clientes Bancários
Este projeto foi desenvolvido para analisar e prever o score de crédito dos clientes de um banco. O objetivo é fornecer uma classificação automática do crédito (Ruim, Ok, Bom) com base em dados de clientes, auxiliando o banco a tomar decisões mais assertivas e eficientes na concessão de crédito.

## Funcionalidades Gerais
- Análise exploratória e tratamento de dados de clientes.
- Treinamento de dois modelos de Machine Learning (Random Forest e KNN) para comparação de desempenho.
- Seleção automática do modelo mais preciso para uso final.
- Análise da importância de cada característica para o score de crédito, ajudando na interpretação dos resultados e decisões de negócio.

## Ferramentas e Tecnologias Utilizadas
- Python: Linguagem de programação para manipulação e análise de dados.
- Pandas: Para tratamento e manipulação dos dados.
- Scikit-learn: Para construção e avaliação de modelos de Machine Learning.
- Jupyter Notebook: Ambiente interativo para desenvolvimento e análise de dados.

## Resultados
- Acurácia: O modelo de Árvore de Decisão obteve a melhor performance, com uma acurácia de 82%, enquanto o KNN apresentou 73%.
- Variáveis Relevantes: As características mais influentes para definir o score de crédito foram "divida_total", "mix_credito" e "juros_emprestimo".
Esses insights permitem à empresa identificar rapidamente o score de crédito e os principais fatores associados ao perfil de crédito de seus clientes, aprimorando a estratégia de concessão de crédito.