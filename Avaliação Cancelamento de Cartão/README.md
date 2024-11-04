# Avaliação dos Motivos de Cancelamento de Cartão
Este projeto analisa dados de clientes para identificar os principais motivos de cancelamento de cartão de crédito. O script importa e trata uma base de dados, realiza análises exploratórias e gera visualizações que ajudam a entender os padrões associados ao cancelamento de cartões.

## Funcionalidades e Estrutura do Projeto
1. Importação e Limpeza dos Dados:
   - Carrega a base de dados de clientes de um arquivo CSV (<code>data-bank.csv</code>).
   - Remove colunas irrelevantes para focar nos dados pertinentes.
   - Remove valores ausentes para assegurar uma análise precisa.
2. Análise Exploratória dos Dados:
   - Exibe informações detalhadas e estatísticas descritivas da tabela.
   - Analisa a qualidade e completude dos dados com <code>info()</code> e <code>describe()</code>.
   - Gera contagens e porcentagens da variável <code>Categoria</code>, que indica o status do cliente (ativo ou cancelado).
3. Geração de Histogramas:
   - Produz histogramas que mostram a relação entre as variáveis e o status de cancelamento do cliente.
   - Cada gráfico é salvo em PDF na pasta <code>HISTOGRAM</code> com um timestamp único para facilitar a organização.
4. Combinação de Gráficos em um PDF:
   - Agrupa todos os histogramas gerados em um único arquivo PDF para facilitar a visualização e a análise.

## Ferramentas e Bibliotecas Utilizadas
- Python: Linguagem de programação principal.
- pandas: Manipulação e análise de dados.
- plotly: Criação de gráficos interativos e exportação de histogramas.
- PyPDF2: Combinação de arquivos PDF.

## Como Executar
1. Pré-requisitos: Instale as bibliotecas necessárias: pandas, plotly, e PyPDF2 (pip install pandas plotly PyPDF2).
2. Execução:
   - Coloque o arquivo <code>data-bank.csv</code> no mesmo diretório do script.
   - Execute o script em Python.
3. Verificação de Resultados:
   - Os histogramas individuais serão salvos na pasta <code>HISTOGRAM</code> em subdiretórios com a data e hora de execução.
   - O PDF final, que agrupa todos os histogramas, estará salvo na mesma pasta, com o nome <code><data_atual>-Histogramas.pdf</code>.

## Exemplos de Uso e Análise
Este projeto facilita a análise de tendências nos cancelamentos de cartões de clientes ao exibir variáveis comparativas em histogramas. Esse processo ajuda a identificar possíveis correlações entre as características dos clientes e o status de cancelamento.

## Resultados Esperados
O projeto gera insights visuais que podem servir de base para uma análise mais aprofundada dos motivos de cancelamento, ajudando a equipe de negócios a tomar decisões informadas sobre retenção de clientes e políticas de fidelização.
