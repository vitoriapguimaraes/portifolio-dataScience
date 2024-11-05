# Exemplo de Extração e Tratamento de Dados para Envio de Relatório por E-mail

Este projeto é um exemplo de extração e tratamento de dados em Python, criado para gerar relatórios de vendas e enviá-los automaticamente por e-mail. Ele usa um arquivo Excel como base de dados, processa informações sobre faturamento, quantidade de produtos vendidos e o ticket médio por loja, e então formata esses dados em um e-mail HTML, enviado automaticamente pelo Microsoft Outlook.

## Funcionalidades

- Importação de Dados: Lê uma planilha Excel contendo os dados de vendas das lojas.
- Cálculos de Indicadores:
  - Faturamento por Loja: Soma o valor final das vendas por loja.
  - Quantidade de Produtos Vendidos por Loja: Totaliza a quantidade de produtos vendidos por loja.
  - Ticket Médio: Calcula o ticket médio de produtos vendidos em cada loja.
- Envio Automático de E-mail: Utiliza o Microsoft Outlook para enviar um e-mail contendo os relatórios formatados.

## Estrutura do Projeto

1. Importação da Base de Dados: Carrega a base de dados de vendas em um DataFrame com pandas.
2. Processamento dos Dados:
    - Calcula o faturamento por loja, agrupando os dados pela coluna ID Loja.
    - Soma a quantidade de produtos vendidos por loja.
    - Calcula o ticket médio dividindo o faturamento total pela quantidade de produtos vendidos para cada loja.
3. Envio de Relatório por E-mail:
    - Utiliza a biblioteca win32com para interagir com o Microsoft Outlook.
    - Gera um e-mail HTML com os dados processados, formatando o relatório em tabelas.
    - Envia o e-mail para o destinatário configurado.

## Ferramentas e Bibliotecas Utilizadas
- Python: Linguagem principal.
- pandas: Manipulação e análise de dados.
- win32com: Automação do Microsoft Outlook para o envio de e-mails.

## Como Executar
1. Pré-requisitos:
    - Instale a biblioteca pywin32 para automação do Outlook (pip install pywin32).
    - Certifique-se de que o Microsoft Outlook está configurado no computador.
2. Configuração de E-mail:
    - Substitua o campo mail.To pelo endereço de e-mail desejado.
    - Verifique e ajuste o arquivo Excel exemplo_vendas.xlsx, que deve conter as colunas ID Loja, Valor Final, e Quantidade.
3. Execução:
    - Execute o script em um ambiente Python compatível.
    - O script carregará o arquivo exemplo_vendas.xlsx, processará os dados e enviará o relatório para o destinatário configurado.

## Teste de Funcionamento
Para testar o funcionamento, foi utilizado o arquivo exemplo_vendas.xlsx, que contém dados simulados de vendas em diferentes lojas.

## Exemplo de Saída de E-mail
O e-mail gerado terá a seguinte estrutura:
- Assunto: "Relatório de Vendas por Loja"
- Corpo do e-mail:
  - Saudação
  - Tabelas com o faturamento, quantidade de produtos vendidos, e ticket médio por loja.
  - Assinatura.

<hr>

Este projeto automatiza a geração de relatórios de vendas e o envio por e-mail, facilitando a análise e compartilhamento de indicadores de desempenho de forma prática e rápida.