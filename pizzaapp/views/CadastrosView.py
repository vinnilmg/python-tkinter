from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from Postgre import Postgre

class Cadastro():

	def __init__(self):
		self.vc = Toplevel() #depende da janela root (principal)
		self.vc.resizable(False, False)
		self.vc.title('Visualizar cadastros')

		#treeview
		self.tree = Treeview(self.vc, selectmode='browse', column=('id', 'usuario', 'senha', 'nivel'), show='headings')

		self.tree.column('id', width=40, minwidth=500, stretch=NO)
		self.tree.heading('#1', text='ID')

		self.tree.column('usuario', width=40, minwidth=500, stretch=NO)
		self.tree.heading('#2', text='Usuario')

		self.tree.column('senha', width=40, minwidth=500, stretch=NO)
		self.tree.heading('#3', text='Senha')

		self.tree.column('nivel', width=40, minwidth=500, stretch=NO)
		self.tree.heading('#4', text='Nivel')
		
		self.tree.grid(row=0, column=0, padx=10, pady=10)

		self.visualizar_cadastros_impl()

		self.vc.mainloop() 

	def visualizar_cadastros_impl(self):
		postgre = Postgre()

		resultado = None
		try:
			with postgre.conn.cursor() as cursor:
				cursor.execute('select id, usuario, senha, nivel from cadastros')
				resultado = cursor.fetchall()
		except Exception as e:
			print('Erro ao executar query: ', e)

		self.tree.delete(*self.tree.get_children()) #deleta treeview

		cadastros = []

		if resultado is not None:
			for linha in resultado:
				cadastros.append(linha[0]) #id
				cadastros.append(linha[1]) #usuario
				cadastros.append(linha[2]) #senha
				cadastros.append(linha[3]) #nivel

				self.tree.insert("", END, values=cadastros, iid=linha[0], tag='1')
				cadastros.clear()

