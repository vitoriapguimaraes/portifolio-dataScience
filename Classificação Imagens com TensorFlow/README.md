# Classificação de Imagens com Redes Neurais Convolucionais e TensorFlow
Este projeto aborda a construção de um modelo de Inteligência Artificial para classificação de imagens em 10 categorias diferentes usando o dataset CIFAR-10. O objetivo é que o modelo consiga identificar e classificar novas imagens de acordo com essas categorias.
O projeto visa responder ao problema de negócio: "Dada uma nova imagem de uma das 10 categorias (airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck), o modelo é capaz de classificá-la corretamente?"

## Tecnologias Utilizadas
- Python
- Bibliotecas:
   - TensorFlow e Keras - para construção e treinamento de redes neurais
   - Matplotlib e PIL - para visualização e manipulação de imagens
   - Numpy - para manipulação de arrays numéricos

## Funcionalidades
1. Carregamento e Pré-processamento de Dados: Carrega o dataset CIFAR-10 e normaliza os valores dos pixels para a mesma escala.
2. Visualização das Imagens: Exibe as imagens do conjunto de treino para análise visual inicial.
3. Construção e Compilação do Modelo: Define uma Rede Neural Convolucional (CNN) com camadas de convolução, pooling e densa para classificação.
4. Treinamento do Modelo: Realiza o treinamento da CNN utilizando o conjunto de dados de treino.
5. Avaliação e Acurácia: Avalia o modelo no conjunto de teste e exibe a acurácia obtida.
6. Classificação de Novas Imagens: Carrega, processa e classifica uma nova imagem, exibindo o resultado.

## Resultados
O modelo é capaz de classificar imagens novas com boa precisão, mostrando a viabilidade de se aplicar redes neurais convolucionais em tarefas de classificação de imagens.