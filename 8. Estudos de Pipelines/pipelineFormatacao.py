# Criação de Pipeline de Extração, Limpeza, Transformação e Enriquecimento de Dados

# Regras de negócio:
# Carregar somente registros com quantidade produzida superior a 10.
# Remover o caracter "ponto" na última coluna do arquivo para evitar que o número seja truncado
# Enriquecer os dados adicionando no destino uma coluna com a margem de lucro de cada produto

# Imports
import csv
import sqlite3

# Função para remover o ponto da última coluna
def remove_ponto(valor):
    return int(round(float(valor.replace('.', '')), 0))

# Abre o arquivo CSV com os dados da produção de alimentos
with open('producao_alimentos.csv', 'r') as file:
    
    # Cria um leitor de CSV para ler o arquivo
    reader = csv.reader(file)

    # Pula a primeira linha, que contém os cabeçalhos das colunas
    next(reader)

    # Conecta ao banco de dados
    conn = sqlite3.connect('db.db')

    # Deleta a tabela existente, se houver
    conn.execute('DROP TABLE IF EXISTS producao')

    # Cria uma nova tabela para armazenar os dados de produção de alimentos com a nova coluna 'margem_lucro'
    conn.execute('''CREATE TABLE producao (
                    produto TEXT,
                    quantidade INTEGER,
                    preco_medio REAL,
                    receita_total INTEGER,
                    margem_lucro REAL
                )''')

    # Insere cada linha do arquivo com quantidade maior que 10 na tabela do banco de dados
    for row in reader:
        if int(row[1]) > 10:
            
            # Remove o ponto do valor da última coluna e converte para inteiro
            row[3] = remove_ponto(row[3])

            # Calcula a margem de lucro bruta com base no valor médio de venda e na receita total e arredonda para duas casas decimais
            margem_lucro = round((row[3] / float(row[1])) - float(row[2]), 2)

            # Insere a linha com a nova coluna 'margem_lucro' na tabela do banco de dados
            conn.execute('INSERT INTO producao (produto, quantidade, preco_medio, receita_total, margem_lucro) VALUES (?, ?, ?, ?, ?)', (row[0], row[1], row[2], row[3], margem_lucro))

    conn.commit()
    conn.close()

print("Job Concluído com Sucesso!")
