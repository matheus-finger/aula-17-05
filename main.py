import tkinter as tk
from tkinter import ttk


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

rotulo = ttk.Label(janela, textvariable=texto_no_rotulo)
botao = ttk.Button(janela, text="Botão", command=clicou_botao)

rotulo.pack()
botao.pack()

# Iniciando o loop
janela.mainloop()