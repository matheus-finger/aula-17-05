import tkinter as tk
from tkinter import ttk
import time
import threading

print("Criando a janela")
janela = tk.Tk()

# janela.title = "Aprendendo a interface"
janela.geometry('500x400')

i = 0
texto_no_rotulo = tk.StringVar(janela,"Clique no botão")

def clicou_botao():
    global i
    i +=1
    global texto_no_rotulo
    texto_no_rotulo.set("Você clicou no botão %i vezes" % i)

def demora():
    print("Começou a coisa demorada")
    time.sleep(5)
    print("Terminou a coisa demorada")

def faz_demorado_paralelo():
    new_thread = threading.Thread(target=demora)
    new_thread.start()

rotulo = ttk.Label(janela, textvariable=texto_no_rotulo)
botao = ttk.Button(janela, text="Botão", command=clicou_botao)
botaoDemora = ttk.Button(janela, text="Demora", command=faz_demorado_paralelo)

rotulo.pack()
botao.pack()
botaoDemora.pack()

# Iniciando o loop
janela.mainloop()