# Análise dos Motivos de Cancelamento de Cartão de Crédito
Este projeto analisa uma base de dados de clientes para identificar os principais fatores associados ao cancelamento de cartões de crédito. Ele combina limpeza de dados, análises exploratórias e visualizações para extrair insights que ajudam a compreender padrões e propor estratégias de retenção.

## Demonstração/Visualização
Os resultados incluem histogramas salvos em PDF, mostrando a relação entre variáveis como renda, limite de crédito e a categoria do cliente (ativo ou cancelado). Um PDF consolidado reúne todos os gráficos para facilitar a análise. Aqui estão alguns deles.

![Tela do sistema](link)

## Principais Tecnologias Utilizadas
- Python: Linguagem de programação principal utilizada no projeto.
- Pandas: Manipulação e análise eficiente de dados tabulares.
- Plotly: Criação de gráficos e visualizações interativas.
- PyPDF2: Manipulação de arquivos PDF para combinar gráficos em um único documento.

## Estrutura do Projeto
```
├── app.py            # Script principal contendo a lógica para importar, tratar, e analisar os dados, além de gerar os gráficos e o PDF consolidado.
├── data-bank.csv     # Base de dados dos clientes utilizada na análise.
└── HISTOGRAM/        # Pasta gerada automaticamente para armazenar os histogramas individuais e o PDF final consolidado.
```

## Como Executar

### Pré-requisitos:
- Certifique-se de ter Python instalado (>= 3.7).
- Instale as dependências necessárias executando:
      ```
      pip install pandas plotly PyPDF2
      ```

### Etapas:
1. Execute o script com:
      ```
      python app.py
      ```

2. Resultados: Os histogramas serão salvos na pasta <code>HISTOGRAM/</code>.

O PDF consolidado será nomeado com a data e hora da execução, como YYYY-MM-DD_HHMMSS-Histogram.pdf.

## Funcionalidades
- Limpeza e Tratamento de Dados: Remoção de colunas irrelevantes e valores ausentes para análises precisas.
- Análises Exploratórias: Estatísticas descritivas e visualizações para identificar padrões nos dados.
- Visualização em Histogramas: Geração de gráficos que mostram a relação entre as variáveis e o status de cancelamento dos clientes.
- Consolidação de Relatórios: Criação de um PDF único com todos os histogramas gerados, facilitando o compartilhamento e a análise.

## Resultados e Conclusões
- Clientes com menor limite de crédito e alta taxa de utilização apresentam maior propensão ao cancelamento.
- Gráficos revelam padrões significativos que podem ajudar a equipe de negócios a identificar pontos críticos e atuar na retenção de clientes.

## Próximos Passos/Melhorias
- Adicionar uma análise preditiva usando modelos de machine learning para prever a probabilidade de cancelamento com base nas características dos clientes.
- Incorporar gráficos interativos diretamente no ambiente web ou Jupyter Notebook para maior acessibilidade.
- Melhorar a interface de execução, permitindo que o script solicite ao usuário o diretório de entrada para maior flexibilidade.

<br>
<hr> 

### Currículos e Documentos
Acesse os arquivos disponíveis na pasta 
[![Documentos](https://img.shields.io/badge/DOCUMENTOS-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.