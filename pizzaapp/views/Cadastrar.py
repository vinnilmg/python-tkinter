from tkinter import *
from tkinter import messagebox
from Postgre import Postgre
import JanelaLogin as jl

class Cadastrar():

	def __init__(self, janela, login, senha):
		self.root = janela
		self.login = login
		self.senha = senha


	def cadastrarImpl(self):
		cod_padrao = 'buibui10'

		if self.cod_seg.get() == cod_padrao:
			if (len(self.login.get()) <= 20) or (self.senha.get() <= 50):

				#print(self.login, self.senha)
				usuario = self.login.get()
				senha = self.senha.get()

				#banco sql
				postgre = Postgre()

				try:
					with postgre.conn.cursor() as cursor:
						cursor.execute("INSERT INTO cadastros(usuario, senha, nivel) VALUES (%s, %s, %s)", (usuario, senha, 1))
						postgre.conn.commit()
					messagebox.showinfo('Cadastro', 'Usuario cadastrado com sucesso.')
					self.root.destroy() #destroi root
					jl.JanelaLogin() #inicia pela tela de login novamente
				except Exception as e:
					print('Erro inserção usuario: ', e)
			else:
				messagebox.showinfo('ERRO', 'Limites ultrapassados.\nUsuario max. 20\nSenha max. 50')
		else:
			messagebox.showinfo('ERRO', 'Codigo de segurança inválido.')

	
	def cadastrar(self):
		Label(self.root, text='Chave de segurança:').grid(row=3, column=0, pady=5, padx=5)
		self.cod_seg = Entry(self.root, show='*')
		self.cod_seg.grid(row=3, column=1, pady=5, padx=10)

		cadastrar = Button(self.root, text='Confirmar cadastro', width=15, bg='blue1', command=self.cadastrarImpl)
		cadastrar.grid(row=4, column=0, columnspan=3, pady=5, padx=10)