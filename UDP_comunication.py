import os, sys
import socket
import time

HOST = 'localhost'
PORT = 5003

TAM_MSG = 128

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))	

class mensagem:
    #def __init__(self, *args):
    #    """ Create a vector, example: v = Vector(1,2) """
    #    if len(args)==0: self.values = (0,0)
    #    else: self.values = args

	def __init__(self):
		self.ID = '-'
		self.ipo = '-'
		self.ipd = '-'
		self.porto = '-'
		self.portd = '-'
		self.MSG = '-'
		self.status = '-'
		self.nome = '-'
		self.grupo = '-'

	def __set__(self, ID, IPO, IPD, PortO, PortD, MSG, status, nome, grupo):
		self.ID = ID
		self.ipo = IPO
		self.ipd = IPD
		self.porto = PortO
		self.portd = PortD
		self.MSG = MSG
		self.status = status
		self.nome = nome
		self.grupo = grupo
	def setid(self, ID):
		self.ID = ID
	def setipo(self, IPO):
		self.ipo = IPO
	def setipd(self, IPD):
		self.ipo = IPD
	def setporto(self, PortO):
		self.porto = PortO
	def setportd(self, PortD):
		self.portd = PortD
	def setmsg(self, MSG):
		self.MSG = MSG
	def setstatus(self, status):
		self.status = status
	def setnome(self, nome):
		self.nome = nome
	def setgrupo(self, grupo):
		self.grupo = grupo

	def getget(self):
		return self.ID, self.ipo, self.ipd, self.porto, self.portd, self.MSG, self.status, self.nome, self.grupo
	def getid(self):
		return self.ID
	def getipo(self):
		return self.ipo
	def getipd(self):
		return self.ipd
	def getporto(self):
		return self.porto
	def getportd(self):
		return self.portd
	def getmsg(self):
		return self.MSG
	def getstatus(self):
		return self.status
	def getnome(self):
		return self.nome
	def getgrupo(self):
		return self.grupo

	def enviarMSG(self):
		MSG = str(self.getid()) + '\t' + str(self.getipo()) + '\t' + str(self.getipd()) + '\t' + str(self.getporto()) + '\t' + str(self.getportd()) + '\t' + str(self.getmsg()) + '\t' + str(self.getstatus() + '\t' + str(self.nome)) + '\t' + str(self.grupo())
		s.sendto(bytes(MSG, 'UTF-8'), (HOST, PORT))	
	def setRECV(self, MSG):
		parametros = MSG.split('\t')
		self.ID 	= 	parametros[0]
		self.ipo 	= 	parametros[1]
		self.ipd 	= 	parametros[2]
		self.porto 	= 	parametros[3]
		self.Portd 	= 	parametros[4]
		self.MSG 	= 	parametros[5]
		self.status = 	parametros[6]
		self.nome 	= 	parametros[7]
		self.grupo 	= 	parametros[8]

	def printf(self):
		print(self.getget())

	# START FILE SYSTEM MANIPULATION 	
	def saveMSG(self, File):
		target = open(File, 'a')
		linha = str(self.getid()) + '\t' + str(self.getipo()) + '\t' + str(self.getipd()) + '\t' + str(self.getporto()) + '\t' + str(self.getportd()) + '\t' + str(self.getmsg()) + '\t' + str(self.getstatus()) + '\t' + str(self.getnome()) + '\t' + str(self.getgrupo() + '\n')
		target.write(linha)
		target.close()
	def recoverMSG(self, File, ID):
		with open(File) as f:
			content = f.readlines()
			f.close()
		for line in content:
			parametros = line.split('\t')
			if parametros[0] == ID:
				self.ID 	= 	parametros[0]
				self.ipo 	= 	parametros[1]
				self.ipd 	= 	parametros[2]
				self.porto 	= 	parametros[3]
				self.Portd 	= 	parametros[4]
				self.MSG 	= 	parametros[5]
				self.status = 	parametros[6]
				self.nome	= 	parametros[7]
				self.grupo 	= 	parametros[8]
			else:
				pass
	def setstatusARQ(self, File, ID, status):
		with open(File) as f:
			content = f.readlines()
			f.close()
		for line in content:
			parametros = line.split('\t')
			if parametros[0] == ID:
				self.status =	status

	# ACHA TRABALHO PARA FAZER & RETORNA A LINHA
	def findWork(self, File, status):
		with open(File) as f:
			content = f.readlines()
			f.close()
		for line in content:
			parametros = line.split('\t')
			if parametros[6] == status:
				recoverMSG(File, parametros[0])

	def listarMSG(self, FileContatos, FileMensagens, nome):
		auxID = ''
		localizounome = 0
		localizoumsg = 0
		# VERIFICA SE EXISTE CONTATO ********
		with open(FileContatos) as f:
			content = f.readlines()
			f.close()
		for line in content:
			parametros = line.split('\t')
			if parametros[7] == nome:
				localizounome += 1
				auxID = parametros[0]
			##print("\n", parametros[7], "  ", parametros, "\n")
			##print("@@@@", localizounome, localizoumsg)
		# MULTIPLOS NOME IGUAIS VAI DAR ERRO
		if localizounome == 1:
			with open(FileMensagens) as f:
				content = f.readlines()
				f.close()
			for line in content:
				parametros = line.split('\t')
				if parametros[0] == auxID:
					localizoumsg += 1
					# IMPRIME A MENSAGEM E STATUS DA MENSAGEM
					print(parametros[5], " ", parametros[6])
			return localizounome, localizoumsg
		elif localizounome > 1:
			return 2, -1
		else:
			return -1, -1


	####$$$$$
	####$$$$$  	SE PRIMEIRA LINHA FOR IGUAL A ZERO ELE DA ERRO
	####$$$$$	
	# PREVER QUE SE FOR GRUPO ADD UM SIMBOLO NO INICIO PARA IDENTIFICAR TAL #####
	def listarContatos(self, FileContatos):
		with open(FileContatos) as f:
			content = f.readlines()
			f.close()
		for line in content:
			parametros = line.split('\t')
			# SE FOR IGUAL A '-' É PORQUE É UM CONTATO NAO GRUPO
			if parametros[8] == '-\n':
				sys.stdout.write(parametros[7])
				sys.stdout.write("\n")
			else:
				sys.stdout.write("   # ")
				sys.stdout.write(parametros[7])
				sys.stdout.write("\n")


	#********************************************************



	def contatoexiste(self, FileContatos, nome):
		localizounome = 0
		with open(FileContatos) as f:
			content = f.readlines()
			f.close()
		for line in content:
			parametros = line.split('\t')
			if parametros[7] == nome:
				localizounome += 1
				auxID = parametros[0]		
		return localizounome

	# x < 1 -> NAO EXISTE GRUPO
	# x = 0 -> EXISTE GRUPO MAS NAO O CONTATO
	# x = 1 -> JA EXISTE CONTATO NO GRUPO
	# x > 1 -> EXISTE MULTIPLOS CONTATOS COM MESMO NOME NESTE GRUPO // NÃO TESTO O IP
	def grupoexiste(self, FileContatos, nome, grupo):
		localizounome = -1
		with open(FileContatos) as f:
			content = f.readlines()
			f.close()
		for line in content:
			parametros = line.split('\t')
			if parametros[7] == nome and parametros[8] == str(grupo+'\n'):
					localizounome += 1
		return localizounome


	# END FILE SYSTEM MANIPULATION


#######################################################################3



def enviarMSG(MSG):
	s.sendto(bytes(MSG, 'UTF-8'), (HOST, PORT))
	return 1
def receberMSG():
	MSG = s.recv(TAM_MSG).decode('UTF-8')
	return MSG

def display():
	print("Selecione uma das funcionalidades abaixo:  \n")
	print("i\t-> Inserir nome\ng\t-> Inserir grupo\nl\t-> Listar Mensagens\ns\t-> Enviar mensagem\nc\t-> Listar contatos\nd\t-> Deletar contato\nH\t-> HELP\n")
	return input()




