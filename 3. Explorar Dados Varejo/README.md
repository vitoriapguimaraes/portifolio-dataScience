# Análise Exploratória de Dados com Python Aplicada ao Varejo
Este projeto realiza uma análise exploratória de dados no setor de varejo, utilizando um dataset com informações de vendas. O objetivo é gerar insights relevantes para a tomada de decisão, aplicando técnicas de manipulação de dados e visualização. A análise permite identificar padrões de comportamento de compra, impactos de descontos e outros fatores que influenciam as vendas.

### Este projeto também está sendo adaptado para visualização na web, com o desenvolvimento em andamento. A versão em processo, utilizando Docker, pode ser encontrada e acessada na pasta [![WebDockerVersion](https://img.shields.io/badge/WebDockerVersion-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-python-dataScience/tree/main/3.%20Explorar%20Dados%20Varejo/WebDockerVersion)).

<br>

## Demonstração/Visualização
A análise inclui gráficos e visualizações detalhadas que mostram tendências de vendas, a relação entre descontos e volume de compras, entre outros insights. Além disso, são feitas simulações com diferentes cenários de preços e descontos para prever impactos nas vendas.

![Tela do sistema](https://github.com/vitoriapguimaraes/portifolio-python-dataScience/blob/main/3.%20Explorar%20Dados%20Varejo/AnaliseExploratoria-Demonstacao.gif)

## Principais Tecnologias Utilizadas
- Python: Linguagem de programação principal
- Pandas: Manipulação de dados
- Matplotlib e Seaborn: Visualizações gráficas
- Jupyter Notebook: Ambiente interativo para desenvolvimento e visualização de resultados

## Estrutura do Projeto
```
├── WebDockerVersion         # Versão do script ajustada para web, utilizando Docker
├── app-analise.py           # Script principal
└── dataset.csv              # Contém o arquivo da base de dados utilizada para análise
```

## Como Executar
- Certifique-se de ter Python instalado (>= 3.7).
- Instale as dependências necessárias executando:

      pip install pandas numpy matplotlib seaborn datetime

### Etapas:
1. Execute o script com:
      ```
      python app-analise.py
      ```

2. Resultados: As respostas das perguntas de negócios estão apresentadas no <code>console</code> e as imagens salvas em <code>images</code>.

## Funcionalidades
- Carregamento e limpeza de dados com Pandas.
- Visualização gráfica das vendas e dos efeitos de descontos com Matplotlib e Seaborn.
- Análise de correlações e tendências de vendas com base em diferentes variáveis.
- Simulação de cenários de preços e descontos para prever impactos nas vendas.

## Resultados e Conclusões
- Identificação de padrões de vendas sazonalidade.
- Análise do impacto de descontos no volume de vendas.
- Gráficos de correlação que mostram a relação entre diferentes fatores (como preço, desconto e volume de vendas).

## Próximos Passos/Melhorias
- Implementar um dashboard interativo para visualização em tempo real.

<br>
<hr> 

### Currículos e Documentos
Acesse os arquivos disponíveis na pasta 
[![Documentos](https://img.shields.io/badge/DOCUMENTOS-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
