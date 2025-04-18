# Portfólio de Projetos: PowerBI
![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=white)
![DAX](https://img.shields.io/badge/DAX-FFB81C?style=for-the-badge&logoColor=white)
![Power Query](https://img.shields.io/badge/Power%20Query-323C6D?style=for-the-badge&logo=microsoft&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-FF6F61?style=for-the-badge&logo=tensorflow&logoColor=white)

Este repositório contém dashboards desenvolvidos no Power BI, com foco em estudos e aplicações práticas. Além disso, inclui conteúdos sobre análise de dados, machine learning, SQL e R, demonstrando como essas ferramentas podem ser usadas de forma integrada para extrair insights e resolver problemas de negócios.

<strong>Abaixo está a lista dos projetos desenvolvidos:</strong>

[![Dashboard Marketing](https://img.shields.io/badge/1.%20Dashboard%20Marketing-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Marketing)<br>
[![Dashboard Comercial](https://img.shields.io/badge/2.%20Dashboard%20Comercial-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Comercial)<br>
[![Dashboard Vendas](https://img.shields.io/badge/3.%20Dashboard%20Vendas-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashborad%20Vendas)<br>
[![Dashboard Geral](https://img.shields.io/badge/4.%20Dashboard%20Geral-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Geral)<br>
[![Dashboard RH](https://img.shields.io/badge/5.%20Dashboard%20RH-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20RH)<br>
[![Dashboard Segmentação](https://img.shields.io/badge/6.%20Dashboard%20Segmentação%20Clientes-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Segmenta%C3%A7%C3%A3o%20Clientes)<br>
[![Dashboard Logística](https://img.shields.io/badge/7.%20Dashboard%20Logística-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Logistica)<br>
[![Dashboard Financeiro](https://img.shields.io/badge/8.%20Dashboard%20Financeiro-black?style=flat-square)]([link](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Financeiro))<br>
[![Dashboard Séries Temporais](https://img.shields.io/badge/9.%20Dashboard%20Séries%20Temporais-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Series%20Temporais)<br>
[![Dashboard Anomalias](https://img.shields.io/badge/10.%20Dashboard%20Anomalias-black?style=flat-square)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Anomalias)


## 1. Dashboard de Marketing

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Marketing/display-dashboardMarketing.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Marketing)

### Estrutura da base de dados

Arquivo DadosMarketing.csv contém inicialmente as seguintes colunas que foram relevantes para construção da análise:
  - ID
  - Comprou
  - Data Cadastro
  - Pais
  - Salario Anual
  - Escolaridade
  - Estado Civil
  - Filhos em Casa
  - Adolescentes em Casa
  - Gasto com Alimentos
  - Gasto com Brinquedos
  - Gasto com Eletronicos
  - Gasto com Moveis
  - Gasto com Utilidades
  - Gasto com Vestuario
  - Numero de Compras na Loja
  - Numero de Compras na Web
  - Numero de Compras via Catalogo
  - Numero Visitas WebSites Mes

Colunas criadas a partir dos dados:
  - TotalGasto

Quantidade total dos dados: 1.999

## 2. Dashboard Comercial

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Comercial/display-dashboardComercial.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Comercial)

### Estrutura da base de dados

Arquivo DadosComercial.csv contém inicialmente as seguintes colunas que foram relevantes para construção da análise:
  - Categoria
  - Estado
  - Fabricantes
  - Loja
  - Segmento
  - Total de Venda
  - Vendedor

Nenhuma nova coluna foi criada a partir dos dados.

Quantidade total dos dados: 457


## 3. Dashboard Analítico de Vendas

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Vendas/display-dashboardVendas.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Vendas)

### Estrutura da base de dados

Arquivo dataset.csv contém inicialmente as seguintes colunas que foram relevantes para construção da análise:

  - ID_Pedido
  - Data_Pedido
  - Desconto
  - Pais
  - Prioridade
  - Categoria
  - SubCategoria
  - Total_Vendas

Nenhuma nova coluna foi criada a partir dos dados.

Quantidade total dos dados: 51.290


## 4. Dashboard Geral (de Vendas, Custo, Margem de Lucro e KPI)

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Geral/display-dashboardGeral.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Geral)

### Estrutura da base de dados
Os seguintes arquivos relacionados foram utilizados:
    - Clientes.csv (1.590 linhas de dados)
    - Pedidos.csv (25.035 linhas de dados)
    - Produtos.csv (10.292 linhas de dados)
    - Vendas.csv (51.290 linhas de dados)

As seguintes colunas foram relevantes para construção da análise:
  - [Clientes] Mercado
  - [Pedidos] Data Pedido
  - [Pedidos] Modo Envio
  - [Produtos] Categoria
  - [Vendas] Valor Venda
  - [Vendas] Custo Envio
  - [Vendas] Lucro
  - [Vendas] MargemLucro

Colunas criadas a partir dos dados:
  - [Vendas] Lucro
  - [Vendas] MargemLucro


## 5. Dashboard Analítico para RH

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20RH/display-dashboardRH.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20RH)

### Estrutura da base de dados
Arquivo dadosRH.csv contém inicialmente as seguintes colunas que foram relevantes para construção da análise:
  - Funcao
  - Genero
  - Satisfacao_Trabalho
  - Envolvimento_Trabalho
  - Disponivel_Hora_Extra

Colunas criadas a partir dos dados:
  - TotalFunc
  - %Funcionarios
  - SalarioMedio
  - ExperienciaMedia

Quantidade total dos dados: 1.400


## 6. Dashboard da Segmentação Inteligente de Clientes com Machine Learning

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Segmenta%C3%A7%C3%A3o%20Clientes/display-dashboardML.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Segmenta%C3%A7%C3%A3o%20Clientes)

### Estrutura da base de dados
Segmentei os clientes em três grupos com base em similaridades para personalizar campanhas de marketing. O dashboard apresenta as médias de idade, renda anual e pontuação de gastos de cada segmento, utilizando técnicas de Machine Learning desenvolvidas em Python. Todo o processo está documentado no arquivo pythonMachineLearningPowerBI.ipynb e os dados utilizados estão no arquivo dadosML.txt:
  - Cluster
  - ID
  - Idade
  - Pontuacao_gastos
  - Renda_anual

 
## 7. Dashboard de Logística

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Logistica/display-dashboardLogistica.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Logistica)

### Estrutura da base de dados
Arquivo dadosLogistica.csv contém inicialmente as seguintes colunas que foram relevantes para construção da análise:
  - Status_Entrega
  - ID_Vendedor
  - ID_Cidade
  - Data_Entrega_Realizada
  - Canal_Entrega
  - Equipe_Entrega

Colunas criadas a partir dos dados:
  - TotalEntregas
  - TotalEntregasPrazo
  - Rating

Quantidade total dos dados: 53.770

## 8. Dashboard de Análise Financeira

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Financeiro/display-dashboardFinanceiro.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Financeiro)

### Estrutura da base de dados
Arquivo dadosFinanceiro.csv contém inicialmente contém as seguintes colunas que foram relevantes para construção da análise:
  - Componente
  - Data

Colunas criadas a partir dos dados:
  - TotalDespesas
  - TotalReceitas
  - Lucro
  - MargemLucro

Quantidade total dos dados: 432


## 9. Dashboard Análise de Series Temporais

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Series%20Temporais/display-dashboardSeriesTemporais.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Series%20Temporais)

### Estrutura da base de dados
Arquivo Producao-2018-2023.xlsx contém inicialmente contém as seguintes colunas que foram relevantes para construção da análise:
  - Total Unidades Produzidas
  - Turno
  - Range Idade Funcionarios
  - Período

Colunas criadas a partir dos dados:
  - Média Móvel do Total Unidades Produzidas

Quantidade total dos dados: 868

## 10. Dashboard de Detecção de Anomalias em Transações Financeiras com Linguagem R

![GIF do dashboard](https://github.com/vitoriapguimaraes/portifolio-PowerBI/blob/main/Dashboard%20Anomalias/display-dashboardAnomalias.gif)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](https://github.com/vitoriapguimaraes/portifolio-PowerBI/tree/main/Dashboard%20Anomalias)

### Estrutura da base de dados
Agrupei as transações financeiras dos clientes usando Machine Learning em linguagem R e detectei possíveis anomalias com base em dados fictícios. O resultado foi apresentado visualmente por meio de gráficos no Power BI, facilitando a identificação de comportamentos atípicos nas transações. Os dados utilizados estão no arquivo dadosNovos.txt:
  - anomaly_score
  - id
  - status


<br>
<hr> 

### Currículos e Documentos
Acesse os arquivos disponíveis na pasta 
[![Documentos](https://img.shields.io/badge/DOCUMENTOS-%F0%9F%93%83-blue?style=flat-square)](https://github.com/vitoriapguimaraes/vitoriapguimaraes/tree/main/DOCUMENTOS) para mais informações sobre minhas qualificações e certificações.


<!-- 
Modelo:

![GIF do dashboard](link)

[![Acesse o Repositório](https://img.shields.io/badge/Acesse%20o%20Reposit%C3%B3rio-gray?style=for-the-badge)](link)

### Estrutura da base de dados
Arquivo dataset.csv contém inicialmente contém as seguintes colunas que foram relevantes para construção da análise:

Nenhuma nova coluna foi criada a partir dos dados. | Colunas criadas a partir dos dados:

Quantidade total dos dados: 

//////

ignore por enquanto, melhorar o dashboard:
- Dashboard Mercado de Ações
-->
