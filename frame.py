from tkinter import *
from tkinter import ttk


janela = Tk()
janela.title('Frame')
janela.geometry('500x500')

frame = Frame(janela, width=300, height=300, bg='white').grid(row=0, column=0)
Label(frame, text='Teste de frame').grid(row=0, column=0)

janela.mainloop() #inicia 