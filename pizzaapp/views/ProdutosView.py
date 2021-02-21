from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
from Postgre import Postgre

class Produtos():

	def __init__(self, janela_root):
		self.tree = Treeview(janela_root, selectmode='browse', column=('column1', 'column2', 'column3', 'column4'), show='headings')

		self.tree.column('column1', width=100, minwidth=500, stretch=NO)
		self.tree.heading('#1', text='Nome')

		self.tree.column('column2', width=200, minwidth=500, stretch=NO)
		self.tree.heading('#2', text='Ingredientes')

		self.tree.column('column3', width=100, minwidth=500, stretch=NO)
		self.tree.heading('#3', text='Grupo')

		self.tree.column('column4', width=100, minwidth=500, stretch=NO)
		self.tree.heading('#4', text='Preço')
		
		self.tree.grid(row=0, column=4, padx=10, pady=10, columnspan=4, rowspan=7)

		self.visualizar_produtos_impl()
		#self.vc.mainloop() 

	def visualizar_produtos_impl(self):
		postgre = Postgre()

		resultado = None
		try:
			with postgre.conn.cursor() as cursor:
				cursor.execute('select nome, ingredientes, grupo, preco, id from produtos')
				resultado = cursor.fetchall()
		except Exception as e:
			print('Erro ao executar query: ', e)

		self.tree.delete(*self.tree.get_children()) #deleta treeview

		produtos = []

		if resultado is not None:
			for linha in resultado:
				produtos.append(linha[0]) 
				produtos.append(linha[1]) 
				produtos.append(linha[2]) 
				produtos.append(linha[3]) 

				self.tree.insert("", END, values=produtos, iid=linha[4], tag='1')
				produtos.clear()


	def excluir_cadastros_impl(self):
		postgre = Postgre()
		id_deletar = int(self.tree.selection()[0])

		try:
			with postgre.conn.cursor() as cursor:
				cursor.execute('delete from produtos where id = %s', (id_deletar, ))
				postgre.conn.commit()
		except Exception as e:
			print('Erro ao executar query METHOD (excluir_cadastros_impl): ', e)

		self.visualizar_produtos_impl()


	def limpar_cadastros_impl(self):

		if messagebox.askokcancel('Limpar dados CUIDADO!!!!', 'Deseja excluir todos os dados?'): #TRUE se sim

			postgre = Postgre()
			try:
				with postgre.conn.cursor() as cursor:
					cursor.execute('truncate table produtos')
					postgre.conn.commit()
			except Exception as e:
				print('Erro ao executar query METHOD (limpar_cadastros_impl): ', e)

		self.visualizar_produtos_impl()