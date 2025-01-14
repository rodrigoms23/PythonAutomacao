#pip install pyautogui

import pyautogui
import time
import pandas as pd
pyautogui.PAUSE = 0.5 #DEFINE O TEMPO DE ESPERA ENTRE OS COMANDO
#pyautogui.click
#pyautogui.press
#pyautogui.write
#pyautogui.hotkey -> atalho de teclado(ctrl,C)

#PASSO 1:ABRIR O SISTEMA DA EMPRESA
#Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press('win')#pressiona tecla win

pyautogui.write('chrome')#escreve chrome

pyautogui.press('enter')

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')

#pedir pro computador esperar 3 segundo por que a pagina pode demorar a carregar
time.sleep(1)
#fazer login
pyautogui.click(x=718, y=368)#manda clicar em uma localização exata
pyautogui.write('rodrigo@gmail.com')
pyautogui.press('tab')#usa o tab para passar de campo e não ter que pegar localizaçoes exatas
pyautogui.write('rodrigo0123')
pyautogui.click(x=937, y=542)

#importar a base de dados dos produtos
base_dados = pd.read_csv('produtos.csv')
time.sleep(2)
#PASSO 4:cadastrar 1 produto


#numero negativo pra baixo numero negativo pra cima
#pyautogui.scroll(10000)
#index = linhas da tabela

 
#PASSO 5:repetir p4 até acabar todos os produtos
for linha in base_dados.index:
    pyautogui.click(x=688, y=255) #clica no primeiro campo
    pyautogui.write(str(base_dados.loc[linha,'codigo']))#nometabela.loc[linha,'coluna']
    pyautogui.press('tab')
    pyautogui.write(str(base_dados.loc[linha,'marca']))
    pyautogui.press('tab')
    pyautogui.write(str(base_dados.loc[linha,'tipo']))
    pyautogui.press('tab')
    pyautogui.write(str(base_dados.loc[linha,'categoria']))
    pyautogui.press('tab')    
    pyautogui.write(str(base_dados.loc[linha,'preco_unitario']))
    pyautogui.press('tab')
    pyautogui.write(str(base_dados.loc[linha,'custo']))
    pyautogui.press('tab')
    if not pd.isna(base_dados.loc[linha,'obs']):
        pyautogui.write(str(base_dados[linha],'obs'))
        
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)

