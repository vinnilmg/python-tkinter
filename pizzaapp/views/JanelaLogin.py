from tkinter import *
from tkinter import messagebox
import psycopg2 as ps
from Cadastrar import Cadastrar
from AdminJanela import AdminJanela
from Postgre import Postgre
from CadastrosView import Cadastro


class JanelaLogin():

	def __init__(self):
		self.postgre = Postgre()
		self.root = Tk()
		#self.root.resizable(True, True)
		self.root.title('Login')

		#Titulo
		Label(self.root, text='Faça o Login').grid(row=0, column=0, columnspan=2)

		#usuario
		Label(self.root, text='Usuário').grid(row=1, column=0)
		self.login = Entry(self.root)
		self.login.grid(row=1, column=1, padx=5, pady=5)

		#senha
		Label(self.root, text='Senha').grid(row=2, column=0)
		self.senha = Entry(self.root, show='*')
		self.senha.grid(row=2, column=1, padx=5, pady=5)

		telaCadastro = Cadastrar(self.root, self.login, self.senha)
		#buttons
		Button(self.root, text='Login', bg='green3', width=10, command=self.verifica_login).grid(row=5, column=0, padx=5, pady=5)
		Button(self.root, text='Cadastrar', bg='orange3', width=10, command=telaCadastro.cadastrar).grid(row=5, column=1, padx=5, pady=5)
		Button(self.root, text='Visualizar cadastros', bg='white', width=17, command=Cadastro).grid(row=6, column=0, columnspan=2, padx=5, pady=5)

		self.root.mainloop()


	def verifica_login(self):
		autentido = False
		usuarioMaster = False

		usuario = self.login.get() #pega da variavel
		senha = self.senha.get()

		result = None
		try:
			with self.postgre.conn.cursor() as cursor:
				cursor.execute("SELECT nivel FROM cadastros where usuario = %s and senha = %s", (usuario, senha))
				result = cursor.fetchone()
		except Exception as e:
			print('erro ao procurar login::: ', e)
 
		if result is not None:
			#print(result)
			nivel = result[0]
			if nivel == 1:
				usuarioMaster = False
			elif nivel == 2:
				usuarioMaster = True

			autenticado = True
		else:
			autenticado = False #usuario nao localizado

		if not autenticado:
			messagebox.showinfo('Login', 'Usuario/senha inválidos.')
		else:
			self.root.destroy() #destroi janela
			if usuarioMaster:
				#messagebox.showinfo('Login', 'Autenticado.')
				AdminJanela()