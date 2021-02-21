from tkinter import *
from tkinter import messagebox
from JanelaVisualizarProdutos import VisualizarProdutos
from Postgre import Postgre

class AdminJanela():

	def __init__(self):
		self.root = Tk()
		self.root.title('ADMIN')
		#self.root.geometry('300x400')

		Button(self.root, text='Pedidos', width=20, bg='#2E4682').grid(row=0, column=0, padx=10, pady=10)
		Button(self.root, text='Cadastros', width=20, bg='#485A88', command=self.cadastrar_produtos).grid(row=1, column=0, padx=10, pady=10)

		self.root.mainloop()


	def cadastrar_produtos(self):
		#nova janela
		self.cadastrar = Tk()
		self.cadastrar.title('Cadastro de produtos')
		self.cadastrar.geometry('900x280')
		self.cadastrar['bg'] = '#524f4f'

		Label(self.cadastrar, text='Cadastre os produtos', bg='#524f4f', fg='white', font="-weight bold -size 20").grid(row=0, column=0, columnspan=4, padx=5, pady=5)

		Label(self.cadastrar, text='Nome', bg='#524f4f', fg='white').grid(row=1, column=0, columnspan=1, padx=5, pady=5)
		self.nome = Entry(self.cadastrar)
		self.nome.grid(row=1, column=1, columnspan=2, padx=5, pady=5)

		Label(self.cadastrar, text='Ingredientes', bg='#524f4f', fg='white').grid(row=2, column=0, columnspan=1, padx=5, pady=5)
		self.ingredientes = Entry(self.cadastrar)
		self.ingredientes.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

		Label(self.cadastrar, text='Grupo', bg='#524f4f', fg='white').grid(row=3, column=0, columnspan=1, padx=5, pady=5)
		#self.grupo = Entry(self.cadastrar)
		#self.grupo.grid(row=3, column=1, columnspan=2, padx=5, pady=5)
		self.grupo_pizza = IntVar(self.cadastrar)
		self.grupo_salgados = IntVar(self.cadastrar)
		c1 =Checkbutton(self.cadastrar, text='Pizza', variable=self.grupo_pizza, onvalue=1,offvalue=0).grid(row=3, column=1)
		c2 =Checkbutton(self.cadastrar, text='Salgados', variable=self.grupo_salgados, onvalue=1, offvalue=0).grid(row=3, column=2)
		#print(self.grupo_pizza.get())
		#print(self.grupo_salgados.get())
		#Checkbutton(self.cadastrar, text='Salgados', variable=self.grupo).grid(row=3, column=3)

		Label(self.cadastrar, text='Preço', bg='#524f4f', fg='white').grid(row=4, column=0, columnspan=1, padx=5, pady=5)
		self.preco = Entry(self.cadastrar)
		self.preco.grid(row=4, column=1, columnspan=2, padx=5, pady=5)

		Button(self.cadastrar, text='Cadastrar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f', command=self.cadastrar_produtos_impl).grid(row=5, column=0, pady=5, padx=5)
		Button(self.cadastrar, text='Excluir', width=15, bg='gray', relief='flat', highlightbackground='#524f4f').grid(row=5, column=1, pady=5, padx=5)
		Button(self.cadastrar, text='Atualizar', width=15, bg='gray', relief='flat', highlightbackground='#524f4f').grid(row=6, column=0, pady=5, padx=5)
		Button(self.cadastrar, text='Limpar produtos', width=15, bg='gray', relief='flat', highlightbackground='#524f4f').grid(row=6, column=1, pady=5, padx=5)

		visualizar_produtos = VisualizarProdutos(self.cadastrar)

		self.cadastrar.mainloop()

	def cadastrar_produtos_impl(self):
		postgre = Postgre()

		#obtendo campos dos entry
		nome = 			self.nome.get()
		ingredientes = 	self.ingredientes.get()
		preco = 		self.preco.get()

		grupo = ''
		#print(self.grupo_pizza.get())
		#print(self.grupo_salgados.get())
		if self.grupo_pizza.get() == 1:
			grupo = 'pizza'
			#self.grupo_pizza = 0
		elif self.grupo_salgados.get() == 1:
			grupo = 'salgados'
			#self.grupo_salgados = False

		try:
			with postgre.conn.cursor() as cursor:
				cursor.execute('INSERT INTO produtos(nome, ingredientes, grupo, preco) values(%s, %s, %s, %s)',
				 (nome, ingredientes, grupo, preco))
				postgre.conn.commit()
		except Exception as e:
			print('Erro ao inserir produtos: ', e)

		visualizar_produtos = VisualizarProdutos(self.cadastrar)

AdminJanela()