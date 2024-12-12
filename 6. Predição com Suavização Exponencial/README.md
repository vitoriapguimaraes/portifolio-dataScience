# Análise de Séries Temporais para Previsão de Vendas com Python e Suavização Exponencial
Este projeto visa a análise e previsão de vendas futuras utilizando técnicas de séries temporais. Com base nos dados históricos de vendas de 2023, aplicamos métodos de suavização exponencial para projetar o total de vendas de janeiro de 2024. A iniciativa busca responder ao seguinte problema de negócio: "É possível prever o total de vendas em janeiro de 2024 a partir dos dados de vendas de 2023?". O objetivo é fornecer uma análise prática e objetiva para apoiar a tomada de decisão empresarial.

## Demonstração/Visualização
Gráficos interativos de séries temporais e previsão de vendas estão incluídos no notebook, destacando a tendência e a projeção para janeiro de 2024.

![Tela do sistema](https://github.com/vitoriapguimaraes/portifolio-python-dataScience/blob/main/6.%20Predi%C3%A7%C3%A3o%20com%20Suaviza%C3%A7%C3%A3o%20Exponencial/PredicaoSuavizacaoExponencial-Demonstracao.gif)

## Principais Tecnologias Utilizadas
- Python: Linguagem de programação principal
- Pandas: Carregamento e análise de dados.
- NumPy: Manipulação de arrays numéricos.
- Matplotlib e Seaborn: Visualização de dados.
- Statsmodels: Modelagem de séries temporais e suavização exponencial

## Estrutura do Projeto
```
├── main.ipynb        # Notebook principal com todo o código de análise, modelagem e previsão.
└── dataset.csv       # Contém o arquivo da base de dados utilizada para análise.
```

## Como Executar

1. Clone o repositório para sua máquina local.

2. Certifique-se de ter o Python 3.8+ instalado.

3. Instale as dependências necessárias com o comando.

4. Abra o notebook <code>main.ipynb</code> em seu ambiente preferido (ex.: Jupyter Notebook, VSCode).

5. Execute as células sequencialmente para reproduzir a análise.

## Funcionalidades
- Pré-processamento de Dados
   - Importação e carregamento de dados de vendas.
   - Conversão de datas para o formato datetime e definição do índice temporal.

- Análise Exploratória de Dados (EDA)
   - Visualização de séries temporais para identificar tendências e sazonalidades.

- Modelagem de Previsão
   - Implementação da Suavização Exponencial Simples com a biblioteca Statsmodels.
   - Avaliação de desempenho do modelo.

- Previsão de Vendas
   - Projeção do total de vendas para janeiro de 2024 com base no modelo treinado.

## Resultados e Conclusões
O modelo de suavização exponencial gerou uma previsão confiável para o total de vendas em janeiro de 2024. Os principais insights incluem:
- Tendência: Identificação de um padrão de crescimento ou queda nas vendas ao longo do ano de 2023.
- Sazonalidade: Reconhecimento de padrões cíclicos que afetam as vendas mensalmente.
- Previsão: O total de vendas previsto para janeiro de 2024 foi exibido no gráfico de projeção.

## Próximos Passos/Melhorias
- Otimização do Modelo: Testar outros métodos de previsão de séries temporais, como ARIMA ou SARIMA.
- Integração com Dashboard: Criar um painel interativo para visualização das previsões em tempo real.
- Automatização do Processo: Implementar uma rotina automática para atualização dos dados e execução do modelo de previsão.
- Documentação e Comentários: Melhorar os comentários no notebook para facilitar a compreensão do fluxo do código por outros desenvolvedores.

<br>
<hr> 

### Currículos e Documentos
Acesse os arquivos disponíveis na pasta 
[![Documentos](https://img.shields.io/badge/DOCUMENTOS-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
