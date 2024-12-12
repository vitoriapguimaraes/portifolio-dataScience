**Análise Exploratória de Dados com Python Aplicada ao Varejo, com Flask**

Este projeto tem como objetivo analisar dados do setor de varejo, extraindo insights valiosos e respondendo a perguntas de negócios. A análise foi disponibilizada via web utilizando Flask para a interface e Docker para garantir portabilidade e compatibilidade entre sistemas.

## Demonstração/Visualização
A aplicação apresenta os resultados de forma interativa por meio de uma interface web, com gráficos e tabelas dinâmicos que respondem a diversas perguntas de negócios.

![Tela do sistema](https://github.com/vitoriapguimaraes/portifolio-python-dataScience/blob/main/3.%20Explorar%20Dados%20Varejo/WebDockerVersion/AnaliseWeb-Demonstacao.gif)

## Principais Tecnologias Utilizadas
- Python: Linguagem de programação utilizada para todo o desenvolvimento do projeto
- Pandas: Biblioteca essencial para análise e manipulação eficiente de dados.
- Matplotlib e Seaborn: Ferramentas poderosas para criação de gráficos e visualizações personalizadas e interativas.
- Flask: Framework web utilizado para disponibilizar a análise de dados e gráficos por meio de uma aplicação acessível via navegador.
- Docker: Tecnologia de containerização que garante a compatibilidade e portabilidade do projeto em diferentes ambientes.

## Estrutura do Projeto
```
├── AppVersion               # Versão original do Projeto
└── WebDockerVersion/        # Versão do script ajustada para web, utilizando Docker
    ├── app/                 # Diretório principal da aplicação Flask
    |   ├── dataFiles/       # Contém o dataset utilizado na análise
    |   ├── static/          # Arquivos estáticos como imagens ou estilos CSS (se aplicável)
    |   ├── templates/       # Arquivos HTML usados para renderizar as páginas web
    |   └── app.py           # Arquivo principal com a implementação da aplicação Flask
    ├── docker-compose.yml   # Configuração do Docker Compose para orquestrar os contêineres do projeto
    ├── Dockerfile           # Configuração para containerização da aplicação
    └── requirements.txt     # Lista de dependências do projeto
```

## Como Executar
1. Clone o repositório.

2. Instale as dependências:
    Se estiver executando localmente:
    ```
    pip install -r requirements.txt
    ```

3. Inicie a aplicação Flask:
        ```
        python app.py
        ```

    A aplicação estará disponível em: http://localhost:5000

4. Utilizando Docker:
- Construa a imagem Docker:
        ```
        docker build -t eda-retail-app .
        ```
- Inicie o container:
        ```
        docker run -p 5000:5000 eda-retail-app
        ```

    Acesse em: http://localhost:5000

## Funcionalidades
- Respostas a perguntas de negócios por meio de visualizações:
        - Pergunta 1: Cidade com maior volume de vendas na categoria "Office Supplies".
        - Pergunta 2: Distribuição total das vendas por data do pedido.
        - Pergunta 3: Estados com maior volume de vendas.
        - Pergunta 4: Top 10 cidades com maior total de vendas.
        - Pergunta 5: Segmentos com maior volume de vendas (gráfico de pizza).
- Interface web para exploração interativa.
- Geração dinâmica de gráficos e tabelas.

## Resultados e Conclusões
- Insights principais:
        - Identificação de "Office Supplies" como um segmento altamente relevante em cidades específicas.
        - Gráficos de linha e barras mostram padrões claros de vendas ao longo do tempo e por localização.
        - Segmentos mais lucrativos apresentados de forma clara e acessível.
- Impacto: Este projeto fornece uma base visual e analítica para tomada de decisão no setor de varejo.

## Próximos Passos/Melhorias
- Implementar funcionalidades adicionais, como filtros dinâmicos para explorar dados diretamente na interface.
- Otimizar o código para processar datasets maiores de forma mais eficiente.
- Expandir as perguntas de negócios para cobrir outros aspectos, como análise de clientes e previsões de vendas.
- Adicionar testes automatizados para garantir a estabilidade do código.

<br>
<hr> 

### Currículos e Documentos
Acesse os arquivos disponíveis na pasta 
[![Documentos](https://img.shields.io/badge/DOCUMENTOS-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.