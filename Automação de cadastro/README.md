# Automação de Cadastro de Produtos em Portal Web
Este projeto automatiza o processo de cadastro de produtos em um portal de vendas. Utilizando um script em Python e a biblioteca PyAutoGUI, o sistema acessa um site, realiza o login e insere os dados de cada produto com base em um arquivo CSV fornecido. Ele é ideal para operações em lote, economizando tempo e reduzindo o risco de erros manuais.

## Funcionalidades Gerais
- Automação de login no portal de vendas.
- Cadastro automatizado de produtos em massa a partir de uma base de dados CSV.
- Personalização de posições de clique para diferentes monitores usando um script auxiliar.

## Ferramentas e Tecnologias Utilizadas
- Python: Linguagem principal para o desenvolvimento do script.
- PyAutoGUI: Biblioteca para automação de cliques e preenchimento de formulários.
- Pandas: Para manipulação e leitura de dados a partir de um arquivo CSV.
- Google Chrome/Microsoft Edge: Navegador onde o script realiza a automação do cadastro.

### Estrutura do Projeto
```python
├── automacao_cadastro.py            # Script principal para automação do cadastro
├── teste_posicao_tela.py            # Script auxiliar para configurar posições de clique
└── produtos.csv                     # Arquivo CSV com dados dos produtos a serem cadastrados
```	

## Como Executar a Automação
1. Configure a Posição de Clique: Execute teste_posicao_tela.py para ajustar as posições de clique para seu monitor.
2. Prepare a Base de Dados: Insira os dados dos produtos no arquivo produtos.csv.
3. Execute o Script Principal:
```python
python automacao_cadastro.py
```
    O sistema abrirá o navegador, fará login no portal e registrará cada produto automaticamente.

## Resultados
Com o script configurado e executado corretamente, todos os produtos da base <code>produtos.csv</code> serão cadastrados automaticamente no portal de vendas, poupando tempo e reduzindo o risco de erros.