from tkinter import *


def calcular():
	#lb2['text'] = 'clicado!'

	#capturando dados
	imc = (float(peso.get())) / (float(altura.get())**2)

	lb_resposta['text'] = round(imc, 2)



#Criação e configuração de janela
janela = Tk() #instanciando a class
janela.title('Calc IMC')
janela.geometry('300x300') #largura x altura
janela.resizable(False, False)

"""
#Labels
Label(janela, text='Sabor', bg='black', fg='white', padx=30, pady=15).grid(row=0, column=0)

#Entrada de dados
Entry(janela, bg='black', fg='white', show='*').grid(row=0, column=1)

#Botões
Button(janela, text="Enviar", bg='black', fg='white', height=3, width=20, command=mostrar).grid(row=0, column=2)

lb2 = Label(janela, text='ainda nao foi clicado')
lb2.grid(row=3, column=2)
"""
lb_titulo = Label(janela, text='IMC')
lb_titulo.grid(row=0, column=0, columnspan=2)

lb1 = Label(janela, text='Peso:')
lb1.grid(row=1, column=0)
peso = Entry(janela)
peso.grid(row=1, column=1)

lb2 = Label(janela, text='Altura:')
lb2.grid(row=2, column=0)
altura = Entry(janela)
altura.grid(row=2, column=1)

Button(janela, text='Calcular', command=calcular).grid(row=3, column=0)

lb_resposta = Label(janela, text='Resposta')
lb_resposta.grid(row=3, column=1)


janela.mainloop() #inicia 