# Análise Exploratória de Dados com Python Aplicada ao Varejo
Este projeto realiza uma Análise Exploratória de Dados (EDA) aplicada ao setor de varejo, utilizando Python. A análise se concentra em responder perguntas de negócios para gerar insights práticos sobre as vendas em diferentes categorias, cidades e períodos.

## Funcionalidades Gerais
- Carregamento e pré-processamento de dados com Pandas.
- Análise exploratória de dados para responder a perguntas estratégicas do setor de varejo.
- Visualização de dados com gráficos diversos, incluindo gráficos de linhas, barras e pizza.
- Exportação de gráficos gerados para um diretório específico.

## Estrutura do Projeto
- Carregamento e inspeção dos dados: Verificação de registros duplicados, valores ausentes e análise descritiva.
- Perguntas de Negócio:
  - Pergunta 1: Identificação da cidade com maior valor de vendas para produtos da categoria "Office Supplies".
  - Pergunta 2: Total de vendas por data do pedido, exibido em gráfico de linha.
  - Pergunta 3: Total de vendas por estado, exibido em gráfico de barras.
  - Pergunta 4: As 10 cidades com maior valor de vendas, exibido em gráfico de barras.
  - Pergunta 5: Segmento com maior valor de vendas, exibido em gráfico de pizza.
  - Pergunta 6: Total de vendas por segmento e por ano.
  - Pergunta 7: Simulação de faixas de desconto com contagem de vendas que receberiam 15% de desconto.
  - Pergunta 8: Média de valor de vendas antes e depois do desconto de 15%.
  - Pergunta 9: Média de vendas por segmento, por ano e por mês, exibido em gráfico de linha.
  - Pergunta 10: Total de vendas por categoria e subcategoria (Top 12), exibido em gráfico de pizza.

## Ferramentas e Tecnologias Utilizadas
- Python: Linguagem de programação principal.
- Pandas: Manipulação e análise dos dados.
- Matplotlib e Seaborn: Visualização de dados.
- Git e GitHub: Controle de versão e hospedagem do código.

## Conhecimentos Aplicados
- Análise Exploratória de Dados (EDA): Inspeção visual e estatística dos dados.
- Manipulação de Dados: Transformações e agrupamentos com Pandas.
- Visualização de Dados: Criação de gráficos informativos para respostas estratégicas.
- Estrutura de Controle: Utilização de condicionais para simulações de desconto.
- Análise Estatística: Cálculo de médias e distribuições de vendas.

## Como Executar a Análise
1. Carregue o dataset dataset.csv com as colunas esperadas, como Cidade, Categoria, Valor_Venda, Data_Pedido, entre outras.
2. Execute o código para gerar as análises e visualizações. Os gráficos serão exportados automaticamente para o diretório Analise de Vendas/images.
3. Confira as respostas às perguntas de negócio nos logs gerados no terminal ou nos gráficos exportados.

## Exemplos de Saídas
- Pergunta 2: Total de vendas por data do pedido representado em um gráfico de linha.
- Pergunta 5: Segmento com maior valor de vendas representado em um gráfico de pizza com as porcentagens.
- Pergunta 10: Gráfico de pizza duplo que mostra a distribuição de vendas entre as principais subcategorias dentro de cada categoria.

<hr>

Este projeto demonstra como a EDA pode ser aplicada para extrair insights valiosos em um ambiente de negócios, usando um fluxo completo de análise com Python.