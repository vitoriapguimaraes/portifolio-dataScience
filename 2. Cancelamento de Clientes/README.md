# Análise e Redução de Cancelamentos de Clientes em Serviço de Assinatura
Este projeto explora uma base de dados com mais de 800 mil registros para identificar os principais motivos de cancelamento de clientes em um serviço de assinatura. Utilizando ferramentas de análise de dados, buscamos compreender padrões comportamentais e propor soluções que possam reduzir a taxa de cancelamentos e aumentar a retenção de clientes.

## Demonstração/Visualização
O projeto gera gráficos interativos que mostram insights como tipos de contratos com maior taxa de cancelamento, relações com atrasos de pagamento e perfil demográfico dos clientes.
![Tela do sistema](link)

## Principais Tecnologias Utilizadas
- Linguagem: Python
- Bibliotecas: Pandas, Plotly
- Ferramentas: Jupyter Notebook

## Estrutura do Projeto
```
├── main.ipynb                   # Notebook principal contendo todo o código e as etapas da análise.
└── cancelamentos-sample.csv     # Contém o arquivo da base de dados utilizada para análise.
```

## Como Executar
1. Configurar o Ambiente: Certifique-se de ter Python 3.8+ instalado.

2. Instale as dependências do projeto usando o comando:
    ```
    pip install pandas plotly notebook
    ```

3. Executar o Notebook: Abra o arquivo <code>main.ipynb</code> em um ambiente Jupyter Notebook ou equivalente.

4. Execute as células sequencialmente para carregar os dados, realizar a análise e gerar as visualizações.

## Funcionalidades
- Análise de Dados: Identifica os fatores associados ao cancelamento de clientes.
- Segmentação: Explora características comportamentais e demográficas.
- Visualizações Gráficas: Gráficos interativos para identificar padrões e insights acionáveis.

## Resultados e Conclusões
Os principais insights incluem:
- Tipo de Contrato: Contratos mensais apresentam maior taxa de cancelamento.
- Atrasos no Pagamento: Clientes com mais de 20 dias de atraso têm maior probabilidade de cancelar.
- Atendimento ao Cliente: Frequência alta de ligações ao call center está associada a uma maior taxa de cancelamento.
- Perfil Demográfico: Clientes acima de 50 anos com baixo gasto total (< R$ 500) são mais propensos ao cancelamento.

Esses resultados podem fundamentar estratégias de retenção personalizadas e melhorias no atendimento.

## Próximos Passos/Melhorias
- Aplicar técnicas de machine learning para prever a propensão ao cancelamento.
- Desenvolver dashboards interativos para monitoramento contínuo.
- Expandir a análise para incluir variáveis adicionais e bases de dados externas.

<br>
<hr> 

### Currículos e Documentos
Acesse os arquivos disponíveis na pasta 
[![Documentos](https://img.shields.io/badge/DOCUMENTOS-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.