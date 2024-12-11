### Exploratory Data Analysis with Python Applied to Retail ###

# Imports
from flask import Flask, render_template_string, render_template
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import io
import base64

app = Flask(__name__)

### Carregando os dados com pandas em Linguagem Python ###
df = pd.read_csv("data_files/dataset.csv")


# ==> Sumário <==
@app.route('/')
def home():
    return render_template('home.html')


# ==> PERGUNTA 1 <==
@app.route("/pergunta1", methods=["GET"])
def question1():

    df_p1 = df[df['Categoria'] == 'Office Supplies']
    df_p1_total = df_p1.groupby("Cidade")["Valor_Venda"].sum()
    cidade_maior_venda = df_p1_total.idxmax()
    df_p1_sorted = df_p1_total.sort_values(ascending=False).to_dict()

    return render_template('text_p1.html', cidade_maior_venda=cidade_maior_venda, df_p1_sorted=df_p1_sorted)


# ==> PERGUNTA 2 <==
@app.route("/pergunta2", methods=["GET"])
def question2():
    
    # Formula resposta
    df['Data_Pedido'] = pd.to_datetime(df['Data_Pedido'], errors='coerce')
    df_p2 = df.groupby("Data_Pedido")["Valor_Venda"].sum().sort_index()

    # Gerar gráfico
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.lineplot(x=df_p2.index, y=df_p2.values, ax=ax)
    ax.set_title("Vendas por Data do Pedido").set_fontsize(14)
    ax.set_xlabel("Data do Pedido").set_fontsize(12)
    ax.set_ylabel("Total do Valor de Venda (R$)").set_fontsize(12)
    plt.rcParams['font.size'] = 8

    # Ajuste dos rótulos do eixo x para não sobrecarregar
    step = max(1, len(df_p2) // 10)
    ax.set_xticks(df_p2.index[::step])
    ax.set_xticklabels(df_p2.index[::step].strftime('%Y-%m-%d'))

    # Salvar a imagem em memória e codificar em base64
    img = io.BytesIO()
    plt.savefig(img, format='png', transparent=True)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()

    # Renderiza o template com a imagem embutida
    return render_template("text_p2.html", img_data=img_base64, df_p2_sorted=df_p2)


# ==> PERGUNTA 3 <==
@app.route("/pergunta3", methods=["GET"])
def question3():

    # Formula resposta
    df_p3 = df.groupby("Estado")["Valor_Venda"].sum().reset_index().sort_values(by="Valor_Venda", ascending=False)
    df_p3_sorted = df_p3.sort_values(by="Valor_Venda", ascending=False)

    # Gerar gráfico
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(data=df_p3_sorted, x='Estado', y='Valor_Venda', ax=ax, palette='husl')
    ax.set_title("Vendas por Estado").set_fontsize(14)
    ax.set_xlabel("Estado").set_fontsize(12)
    ax.set_ylabel("Total do Valor de Venda (R$)").set_fontsize(12)
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.rcParams['font.size'] = 8

    # Salvar a imagem em memória e codificar em base64
    img = io.BytesIO()
    plt.savefig(img, format='png', transparent=True)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()

    # Renderiza o template com a imagem embutida
    return render_template("text_p3.html", img_data=img_base64, df_p3_sorted=df_p3_sorted)


# ==> PERGUNTA 4 <==
@app.route("/pergunta4", methods=["GET"])
def question4():

    # Formula resposta
    df_p4 = df.groupby("Cidade")["Valor_Venda"].sum().reset_index().sort_values(by="Valor_Venda", ascending = False)[0:10]

    # Gerar gráfico
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.barplot(data=df_p4,
            x = 'Cidade',
            y = 'Valor_Venda',
            hue= 'Cidade',
            palette=sns.color_palette("Set1", n_colors=10, as_cmap=False),
            dodge=False,
            legend=False)
    ax.set_title("As 10 Cidades com Maior Total de Vendas").set_fontsize(14)
    ax.set_xlabel("Cidade").set_fontsize(12)
    ax.set_ylabel("Total do Valor de Venda (R$)").set_fontsize(12)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Salvar a imagem em memória e codificar em base64
    img = io.BytesIO()
    plt.savefig(img, format='png', transparent=True)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()

    # Renderiza o template com a imagem embutida
    return render_template("text_p4.html", img_data=img_base64, df_p4=df_p4)

# ==> QUESTÃO 5 <==
@app.route("/pergunta5", methods=["GET"])
def question5():
    # Agrupando e somando vendas por segmento
    df_p5 = df.groupby("Segmento")["Valor_Venda"].sum().reset_index().sort_values(by='Valor_Venda', ascending=False)
    df_p5['Valor_Venda_Formatado'] = df_p5['Valor_Venda'].apply(lambda x: f'{x:,.2f}')
    df_p5_lista = df_p5["Segmento"].tolist()
    segmento_maior_venda = df_p5_lista[0]

    # Função para formatar os percentuais no gráfico
    def autopct_format(values):
        def my_format(pct):
            total = sum(values)
            val = int(round(pct * total / 100.0))
            return f'{pct:.1f}%\nR$ {val:,.0f}'
        return my_format

    # Gerando o gráfico de pizza
    plt.figure(figsize=(15, 8))
    plt.pie(df_p5["Valor_Venda"],
            labels=df_p5['Segmento'],
            autopct=autopct_format(df_p5['Valor_Venda']),
            startangle=90)
    plt.title("Segmentos com Maiores Vendas")
    plt.axis('equal')

    # Adicionando um círculo central para o gráfico de pizza
    centre_circle = plt.Circle((0, 0), 0.88, fc='white')
    fig = plt.gcf()
    fig.gca().add_artist(centre_circle)

    # Salvando a imagem em memória e codificando em base64
    img = io.BytesIO()
    plt.savefig(img, format='png', transparent=True)
    img.seek(0)
    img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')
    plt.close()

    # Renderizando o template com a imagem embutida
    return render_template("text_p5.html", img_data=img_base64, df_p5=df_p5, df_p5_lista=df_p5_lista, segmento_maior_venda=segmento_maior_venda)







if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)