# Automação de backup

Este projeto é um script em Python que realiza o backup automático de arquivos e diretórios. Utilizando bibliotecas nativas do Python, ele permite selecionar uma pasta e fazer cópias dos arquivos contidos nela, organizando-os por data e hora da criação do backup. Ideal para manter uma cópia segura dos arquivos, este script é configurado para simplificar o processo de backup em um ambiente local.

## Funcionalidades

- Seleção do Diretório de Backup: Utiliza a biblioteca tkinter para abrir uma janela e permitir que o usuário escolha a pasta que deseja fazer backup.
- Criação de Diretório por Data: Nomeia as pastas de backup com base na data e hora do momento de criação do backup, facilitando a organização cronológica.
- Cópia de Arquivos e Pastas: Identifica arquivos e subdiretórios dentro da pasta selecionada e os copia para o diretório de backup.
- Notificação ao Concluir: Exibe uma mensagem no terminal confirmando a conclusão do backup.

## Estrutura do Projeto

1. Seleção de Pasta: A pasta principal de onde os arquivos serão copiados é selecionada via uma janela de seleção.
2. Configuração do Nome e Data: Define o nome e o formato de data para organizar as pastas de backup.
3. Execução do Backup: Verifica cada item da pasta selecionada:
    - Se for um arquivo, copia para a pasta de backup.
    - Se for uma pasta (subdiretório), copia todos os itens contidos nela.
4. Mensagem de Confirmação: Exibe no terminal uma mensagem com a data e a hora do backup concluído.

## Ferramentas e Bibliotecas Utilizadas
- Python: Linguagem principal.
- tkinter: Para interface de seleção de diretórios.
- shutil: Para copiar arquivos e diretórios.
- datetime: Para formatar a data e hora de criação do backup.

## Como Executar
1. Execute o script em um ambiente que permita a utilização de interfaces de seleção de arquivos, como o Jupyter Notebook ou o terminal em um sistema operacional com suporte gráfico.
2. Selecione a pasta que deseja fazer backup na janela que será aberta.
3. Ao finalizar, o script exibirá uma mensagem no terminal indicando a conclusão do backup, com a data e hora.

## Teste de Funcionamento
Para verificar o funcionamento do script, foi feito o backup da pasta “teste”, garantindo que todos os arquivos e subdiretórios contidos nela fossem copiados para o novo diretório de backup, identificado pela data e hora.

## Exemplo de Saída
<code>The backup 2024-10-31 180400 has been completed.</code>
<p>Neste exemplo, o backup foi concluído em 31 de outubro de 2024, às 18h04min.</p>

<hr>

Este projeto facilita a criação de backups periódicos e organizados em pastas com data e hora, permitindo que o usuário mantenha suas informações seguras e bem organizadas.
