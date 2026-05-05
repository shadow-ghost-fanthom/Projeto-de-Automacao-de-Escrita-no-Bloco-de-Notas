# -- Uma automação simples de python onde utilizo as bibliotecas pyautogui, time, keyboard e os.
# -- Este codigo serve para automatizar a escrita de linhas no bloco de notas, onde você pode adicionar o que quer escrito
# -- Em cada linha ou apenas escrever algo que se repete em varias linhas.

import pyautogui, time, keyboard, os
# -- Faz a lista dos textos que vai adicionar.
lista = []
try: 
    esc = int(input("Escreva quantos textos quer adicionar a lista\n>> "))
    if esc > 0:
        for i in range(1, esc + 1):
            os.system('cls' if os.name == 'nt' else 'clear')
            add = input("Escreva o que quer adicionar(Sem acentos!)\n>> ")
            lista.append(add)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        exit()
    os.system('cls' if os.name == 'nt' else 'clear')
    print('-=' * 25)
    print(f"{'Aperte [esc] para poder encerrar o comando':^50}")
    print('-=' * 25)
except ValueError:
    print("Você não digitou um valor válido")
    exit()

# -- Inicia a escrita
while True:
    if keyboard.is_pressed('win'): # -- Prepara o terreno abrindo o bloco de notas | Recomendado utilizar antes do f2.
        time.sleep(2)
        pyautogui.write("bloco de notas", interval=0.1)
        pyautogui.press('enter')

    elif keyboard.is_pressed("f2"): # -- Quando "f2" for pressionado ele escreve a lista(Com o bloco de notas na aba claro).
        time.sleep(1)
        pyautogui.click(x=242, y=149, duration=1)
        time.sleep(1)
        for i in lista:
            pyautogui.write(i, interval=0.1)
            time.sleep(0.5)
            pyautogui.press('Enter')

    elif keyboard.is_pressed("esc"): # -- O loop acaba quando o "esc" é apertado.
            pyautogui.hotkey("win", "d")
            exit()
    time.sleep(0.1)