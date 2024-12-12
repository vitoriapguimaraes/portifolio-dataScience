**Análise Exploratória de Dados com Python Aplicada ao Varejo, com Flask**

Este projeto envolveu o estudo de uma base de dados do setor de varejo, com o objetivo de extrair insights e gerar gráficos informativos. Para facilitar o acesso aos resultados e gráficos, a análise foi disponibilizada via web utilizando Flask e Docker para compatibilidade e portabilidade.

![Tela do sistema](link)

- Passos Realizados:

    - Estudo da Base de Dados: Realizamos uma análise exploratória de dados (Exploratory Data Analysis - EDA) de uma base de dados real do setor de varejo.
        - Objetivo: Obter insights sobre as vendas, identificar padrões de compra, e analisar os dados por localização, segmento e categoria de produto.
        - Ferramentas: Python, pandas, seaborn, matplotlib.
    
    - Extração de Insights: O EDA revelou informações cruciais, como:
            - Qual cidade possui o maior volume de vendas de produtos na categoria “Office Supplies”.
            - Distribuição total das vendas por estado e por data do pedido.
            - Segmentos com maior volume de vendas, com visualizações em gráficos de barras e pizza.
    
    - Geração de Gráficos Informativos: Foram criados gráficos em Python usando matplotlib e seaborn, com um total de 10 perguntas de negócios respondidas, cada uma sendo exibida em um endpoint separado.
    
    - Compatibilidade com Flask e Docker: Para permitir a visualização web dos resultados:
            Flask foi usado para construir a aplicação web, servindo gráficos e tabelas geradas dinamicamente.
            Docker foi utilizado para containerizar a aplicação, garantindo compatibilidade entre sistemas e facilitando o compartilhamento do projeto.