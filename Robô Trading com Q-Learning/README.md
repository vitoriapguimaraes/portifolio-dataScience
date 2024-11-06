# Robô Trading com Inteligência Artificial usando Q-Learning em Python
Este projeto desenvolve um robô de trading usando Q-Learning para realizar operações de compra e venda de ações com o objetivo de maximizar o lucro a partir de um saldo inicial. A aplicação é construída em Python e utiliza dados reais da ação da Apple, baixados do dataset público do Plotly.

## Tecnologias Utilizadas
- Python
- Bibliotecas:
   - Pandas e Numpy: para manipulação e processamento dos dados
   - Plotly: para visualização dos dados com gráficos candlestick
   - Q-Learning: técnica de Reinforcement Learning para aprender a executar ações de negociação

## Funcionalidades e Execução do Projeto
1. Carregamento e Visualização dos Dados
   - O projeto começa com o carregamento dos dados históricos das ações da Apple.
   - Utiliza-se um gráfico candlestick para visualizar a movimentação dos preços ao longo do tempo, oferecendo insights iniciais sobre a dinâmica do mercado.
2. Definição e Configuração do Algoritmo Q-Learning
   O Q-Learning é configurado para treinar o robô de trading com base nos preços históricos.
   Três ações estão disponíveis para o robô: comprar, vender, e manter. Alguns parâmetros do Q-Learning incluem:
      - Número de episódios: Define quantas vezes o modelo será treinado.
      - Alfa (Taxa de aprendizado): Controla o quanto o novo aprendizado sobrepõe o antigo.
      - Gama (Fator de desconto): Determina o valor das recompensas futuras em relação às atuais.
      - Epsilon (Exploração-exploração): Define a probabilidade de escolher uma ação aleatória versus a melhor ação conhecida.
3. Treinamento do Robô de Trading
   O treinamento é realizado por meio de episódios, onde o robô toma decisões (compra, venda ou manutenção) com base na política epsilon-greedy. A função <code>executar_acao()</code> é responsável por simular o efeito de cada ação no saldo e no número de ações, enquanto o Q-Learning ajusta os valores na tabela Q para otimizar a política de negociação ao longo dos episódios.
4. Teste e Avaliação do Robô
   Após o treinamento, o robô é testado com um saldo inicial e decide automaticamente sobre as operações de compra e venda com base na tabela Q aprendida. Ao final, o saldo e o número de ações restantes são usados para calcular o lucro obtido, comparando com o saldo inicial.
5. Resultado Final
   O robô exibe o lucro obtido a partir do saldo inicial após todas as operações simuladas.

## Resultados
O robô final apresenta o saldo e o lucro acumulado após as operações de trading, demonstrando como o Q-Learning pode ser aplicado para tomadas de decisão em operações financeiras.