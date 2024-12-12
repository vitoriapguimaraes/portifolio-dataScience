# Predição do Valor de Aluguel de Imóveis com Regressão Linear
Este projeto aplica técnicas de Regressão Linear Simples para investigar a relação entre a área dos imóveis (em metros quadrados) e o valor do aluguel em uma cidade. O objetivo é prever o valor do aluguel a partir da área do imóvel, utilizando análise estatística e visualização de dados para interpretar os resultados.

## Demonstração/Visualização
Os resultados são apresentados por meio de gráficos que incluem distribuições dos dados, análise de correlação e a linha de regressão ajustada sobre os dados reais, permitindo a visualização do desempenho do modelo.

![Tela do sistema](https://github.com/vitoriapguimaraes/portifolio-python-dataScience/blob/main/4.%20Predi%C3%A7%C3%A3o%20com%20Regress%C3%A3o%20Linear/PredicaoRegressaoLinear-Demonstracao.gif)

## Principais Tecnologias Utilizadas
- Python: Linguagem de programação principal
- Pandas: Manipulação e tratamento de dados tabulares, essencial para preparar o conjunto de dados.
- Matplotlib e Seaborn: Criação de visualizações gráficas informativas, como distribuições de variáveis e gráficos de regressão.
- Statsmodels: Implementação e análise do modelo de Regressão Linear Simples, com cálculos estatísticos detalhados.

## Estrutura do Projeto
```
├── main.ipynb        # Notebook principal contendo toda a análise exploratória, construção
|                       do modelo de regressão linear e interpretação dos resultados.
└── dataset.csv       # Contém o arquivo da base de dados utilizada para análise.
```

## Como Executar
1. Clone o repositório para sua máquina local.

2. Certifique-se de ter o Python 3.8+ instalado.

3. Instale as dependências necessárias com o comando:
    ```
    pip install -r requirements.txt
    ```

4. Abra o notebook main.ipynb em seu ambiente preferido (ex.: Jupyter Notebook, VSCode).

5. Execute as células sequencialmente para reproduzir a análise.

## Funcionalidades
- Análise Exploratória de Dados: Visualização de distribuições e correlação entre variáveis.
- Modelo de Regressão Linear Simples: Construção e avaliação do modelo estatístico.
- Interpretação de Resultados: Apresentação do coeficiente de determinação (R²) e visualização da linha de regressão ajustada.

## Resultados e Conclusões
- O coeficiente de determinação (R²) indica que a variável <code>area_m2</code> explica parte da variabilidade do <code>valor_aluguel</code>, mas outros fatores provavelmente influenciam significativamente o valor do aluguel.
- Sugere-se considerar variáveis adicionais (ex.: localização, número de quartos) para aumentar a precisão do modelo.

## Próximos Passos/Melhorias
- Incluir novas variáveis no modelo para capturar mais fatores determinantes do valor do aluguel.
- Implementar Regressão Linear Múltipla.
- Testar modelos de machine learning para comparação de desempenho.

<br>
<hr> 

### Currículos e Documentos
Acesse os arquivos disponíveis na pasta 
[![Documentos](https://img.shields.io/badge/DOCUMENTOS-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.
