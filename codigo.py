#pip install pyautogui

import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.5 #DEFINE O TEMPO DE ESPERA ENTRE OS COMANDO
#pyautogui.click
#pyautogui.press
#pyautogui.write
#pyautogui.hotkey -> atalho de teclado(ctrl,C)

#Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.press('win')#pressiona tecla win

pyautogui.write('chrome')#escreve chrome

pyautogui.press('enter')

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press('enter')

#pede pro computador esperar 1 segundo,pagina pode demorar a carregar
time.sleep(1)
#fazer login
pyautogui.click(x=718, y=368)#manda clicar em uma localização exata
pyautogui.write('rodrigo@gmail.com')
pyautogui.press('tab')#usa o tab para passar de campo e não ter que pegar localização exata
pyautogui.write('rodrigo0123')
pyautogui.click(x=937, y=542)

#importar a base de dados dos produtos
base_dados = pd.read_csv('produtos.csv')
time.sleep(2)


#numero negativo scroll >baixo 
#numero positivo scroll -> cima
#index = linhas da tabela

 
#cadastrar todos os produtos
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

    if not pd.isna(base_dados.loc[linha,'obs']):   #Verifica se o campo é diferente de nan,se for ele escreve
        pyautogui.write(str(base_dados[linha],'obs'))
        
    pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.scroll(10000)

