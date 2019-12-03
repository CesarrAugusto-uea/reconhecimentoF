from tkinter import Entry, StringVar
import treinamento
import reconhecedorlbph
import teste_opencv
import cv2
import numpy as np
from tkinter import *
from banco import conexao

#var1 = StringVar()

def abrirJanela2():
    janela2 = Tk()

    legenda = Label(janela2,text="Informe seu nome:")
    legenda.place(x=50,y=50)

    nome = Entry(janela2,width=20, font="Arial 15", textvariable = var1)
    nome.place(x=50,y=100)
    var2 = var1.get()
    conexao.execute("INSERT INTO dados(nome) VALUES(?)", (var2))


    salvar = Button(janela2,width=20,text="Salvar", command= lambda: teste_opencv.cadastroRosto())
    salvar.place(x=50,y=150)

    janela2.geometry("300x300+200+200")
    janela2.mainloop()




#------------------------------------------------#

janela = Tk()


cadastrar = Button(janela, width=20, text="Cadastrar", command=lambda: abrirJanela2())
cadastrar.place(x=90,y=50)

treinar = Button (janela, width=20, text="Treinamento", command=lambda: treinamento.treinarAlgo())
treinar.place(x=90,y=100)

reconhecer = Button (janela, width=20, text="Reconhecer", command=lambda: reconhecedorlbph.reconheceRosto())
reconhecer.place(x=90,y=150)

janela.geometry("300x300+200+200")
#janela["bg"] = "black"
janela.title("Menu")
janela.mainloop()


#------------------------------------------------#
