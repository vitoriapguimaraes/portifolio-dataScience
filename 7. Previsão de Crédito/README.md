# Sistema de Previsão de Score de Crédito para Clientes Bancários
Este projeto visa a previsão do score de crédito de clientes bancários, classificando-os de forma automática em categorias de crédito (Ruim, Ok, Bom). Com base nos dados dos clientes, o sistema ajuda o banco a tomar decisões mais assertivas e eficientes para a concessão de crédito. O objetivo é criar um processo mais ágil e transparente, apoiando o banco na análise de risco.

## Demonstração/Visualização
O notebook inclui visualizações gráficas da distribuição de scores, análise de variáveis importantes e comparação de desempenho entre os modelos de previsão.

![Tela do sistema](https://github.com/vitoriapguimaraes/portifolio-python-dataScience/blob/main/7.%20Previs%C3%A3o%20de%20Cr%C3%A9dito/PrevisaoCredito-Demonstracao.gif)

## Principais Tecnologias Utilizadas
- Python: Linguagem de programação principal
- Pandas: Carregamento e análise de dados.
- Matplotlib e Seaborn: Visualização de dados.
- Scikit-learn: Construção e avaliação de modelos de Machine Learning

## Estrutura do Projeto
```
├── main.ipynb        # Notebook principal com a análise exploratória, modelagem e avaliação de desempenho.
└── dataset.csv       # Contém o arquivo da base de dados utilizada para análise.
```

## Como Executar

1. Clone o repositório para sua máquina local.

2. Certifique-se de ter o Python 3.8+ instalado.

3. Instale as dependências necessárias com o comando.

4. Abra o notebook <code>main.ipynb</code> em seu ambiente preferido (ex.: Jupyter Notebook, VSCode).

5. Execute as células sequencialmente para reproduzir a análise.

## Funcionalidades
- Análise Exploratória de Dados (EDA)
  - Carregamento, tratamento e transformação dos dados dos clientes.
  - Visualização de distribuição de variáveis para identificar padrões relevantes.
- Treinamento de Modelos
  - Comparativo entre dois modelos de Machine Learning: Random Forest e KNN.
  - Seleção automática do modelo de melhor desempenho.
- Interpretação dos Resultados
  - Identificação das variáveis mais relevantes para o score de crédito.
  - Visualização de gráficos de importância de variáveis.
- Previsão de Score
  - Classificação automática dos clientes em "Ruim", "Ok" ou "Bom".

## Resultados e Conclusões
Os principais resultados incluem:
- Acurácia do Modelo: O Random Forest obteve uma acurácia de 82%, superando o KNN, que atingiu 73%.
- Variáveis Relevantes: As três variáveis mais influentes para o score de crédito foram "divida_total", "mix_credito" e "juros_emprestimo".
- Impacto do Projeto: A previsão automática do score permite ao banco identificar rapidamente o perfil de risco dos clientes, possibilitando uma concessão de crédito mais eficiente.

## Próximos Passos/Melhorias
- Otimização de Modelos: Avaliar modelos mais robustos, como XGBoost ou LightGBM.
- Integração com o Sistema Bancário: Permitir que a previsão do score seja acessada em tempo real por meio de uma API.
- Expansão do Conjunto de Dados: Incorporar mais variáveis que possam impactar a análise do perfil de crédito.
- Melhor Documentação: Aprimorar os comentários e a documentação do código para facilitar a manutenção futura.

<br>
<hr> 

### Currículos e Documentos
Acesse os arquivos disponíveis na pasta 
[![Documentos](https://img.shields.io/badge/DOCUMENTOS-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
