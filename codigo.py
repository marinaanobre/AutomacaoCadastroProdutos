import pyautogui
import pandas as pd
import time
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')
time.sleep(2)
pyautogui.click(x=788, y=448)
time.sleep(2)
pyautogui.write(link)
pyautogui.press('enter')
time.sleep(3)

pyautogui.click(x=571, y=369)  
pyautogui.write('teste.automacao@email.com')
pyautogui.press('tab')
pyautogui.write('12345')
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(3)

tabela = pd.read_csv("produtos.csv")
print(tabela)

for linha in tabela.index:
    pyautogui.click(x=589, y=254)
    codigo = tabela.loc[linha, "codigo"] 
    pyautogui.write(str(codigo))
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

    obs = tabela.loc[linha, "obs"] 
    if not pd.isna(obs): 
        pyautogui.write(str(obs))

    pyautogui.press("tab") 
    pyautogui.press("enter") 
    pyautogui.scroll(5000)