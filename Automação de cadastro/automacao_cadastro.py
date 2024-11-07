# Automação de Cadastro de Produtos em Portal Web

# Detalhe: para reproduzir o sistema, configure as posições de acordo com seu
# monitor com auxilio do programa em "teste_posicao_tela"

import pyautogui
import pandas as pd
import time

# Carregar a base de produtos
tabela = pd.read_csv("Automação de cadastro/produtos.csv")

print("\nPrimeiras linhas da tabela de produtos")
print(tabela.head())
print("\nÚltimas linhas da tabela de produtos")
print(tabela.tail())

print(f"-"*50)

# Definir tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 0.5

# Abrir sistema (para o problema: abrir o googlechrome)
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Esperar 3 segundos para o site carregar
time.sleep(3)

# Fazer login
pyautogui.click(x=607, y=508)
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("senhateste")
pyautogui.press("tab")
pyautogui.press("enter")

# Percorrer as linhas da tabela: para cada linha é cadastrado um produto
for linha in tabela.index:
  pyautogui.click(x=619, y=353)
  pyautogui.write(str(tabela.loc[linha, "codigo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "marca"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "tipo"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "categoria"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
  pyautogui.press("tab")
  pyautogui.write(str(tabela.loc[linha, "custo"]))
  pyautogui.press("tab")
  if not pd.isna(tabela.loc[linha, "obs"]):
    pyautogui.write(str(tabela.loc[linha, "obs"]))
  pyautogui.press("tab")
  pyautogui.press("enter")
  pyautogui.scroll(5000)