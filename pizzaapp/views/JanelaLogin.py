from tkinter import *

class JanelaLogin():
	def __init__(self):
		self.root = Tk()
		self.root.title('Login')

		#Titulo
		Label(self.root, text='Faça o Login').grid(row=0, column=0, columnspan=2)

		#usuario
		Label(self.root, text='Usuário').grid(row=1, column=0)
		self.login = Entry(self.root)
		self.login.grid(row=1, column=1, padx=5, pady=5)

		#senha
		Label(self.root, text='Senha').grid(row=2, column=0)
		self.senha = Entry(self.root)
		self.senha.grid(row=2, column=1, padx=5, pady=5)

		#buttons
		Button(self.root, text='Login', bg='green3', width=10).grid(row=3, column=0, padx=5, pady=5)
		Button(self.root, text='Cadastrar', bg='orange3', width=10).grid(row=3, column=1, padx=5, pady=5)
		Button(self.root, text='Visualizar cadastros', bg='white', width=17).grid(row=4, column=0, columnspan=2, padx=5, pady=5)

		self.root.mainloop()



JanelaLogin()