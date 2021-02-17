from tkinter import *
from tkinter import ttk


janela = Tk()
janela.title('Treeview')

tree = ttk.Treeview(janela, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')


tree.column('column1', width=200, minwidth=50, stretch=NO)
tree.heading('#1', text='Nome')

tree.column('column2', width=100, minwidth=50, stretch=NO)
tree.heading('#2', text='Idade')

tree.column('column3', width=300, minwidth=50, stretch=NO)
tree.heading('#3', text='Endereço')

tree.column('column4', width=200, minwidth=50, stretch=NO)
tree.heading('#4', text='ID')

elementos = ['Joaquim', '13', 'Rua Celso vieira 718', 1]
tree.insert('', END, values=elementos, tag='1')

tree.grid(row=0, column=0)

janela.mainloop() #inicia 
