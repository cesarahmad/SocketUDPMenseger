#! usr/bin/python

import os, sys
import socket
import time

HOST = 'localhost'
PORT = 5636

TAM_MSG = 128

MSG_RECEBIDO = ''

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))


def displayF():
	print("Selecione uma das funcionalidades abaixo: \n")
	print(" i \t-> Inserir Nome\n g \t-> Inserir Grupo\n l \t-> Listar Mensagens\n s \t-> Enviar Mensagem\n c \t-> Listar Contatos\n d \t-> Deletar Contato\n H \t-> HELP\n")	

def enviarM(MSG):
	s.sendto(bytes(MSG, 'UTF-8'), (HOST,PORT))
	return 1
def receberM():
	MSG = s.recv(TAM_MSG).decode('UTF-8')
	return MSG

def OpenWriteClose(arquivo, linha):
	# 'a' to append 'w' to over write 'r' to read
	target = open(arquivo, 'a')
	target.write(linha)
	target.close()
def Fileprint(file):
	f = open(file, 'r')
	for each_line in f:
		sys.stdout.write(each_line) #IMPRIME SEM NOVA LINHA
	f.close()


def displayL(FileCONTATO, FILEMSG, contato):
	locate = 0
	aux = 0
	with open(FileCONTATO) as fc:
		contentCONTATO = fc.readlines()
		fc.close()
	with open(FILEMSG) as fm:
		contentMSG = fm.readlines()
		fm.close()

	for line in contentCONTATO:
		locate = line.find(contato)
		# ACHOU USUARIO
		if locate > 0:
			# VERIFICAR SE É USUARIO OU GRUPO 
			if line[0] == '#':
				# SE FOR USUARIO IMPRIME MENSAGENS				
				print("USUARIO   ", line)
			else:
				print("GRUPO     ", line)




# TEM QUE RECEBER O NOME DO CONTATO OU GRUPO
def displayM(file):
	f = open(file, 'r')
	for each_line in f:
		sys.stdout.write(each_line) #IMPRIME SEM NOVA LINHA
	f.close()
# 
def addGRUPO(File, GRUPO, MSG):
	content = ''
	aux = 0
	achei = 0
	with open(File) as f:
		content = f.readlines()
		f.close()
	#print("\n\n CONTENTE ANTES", content, "\n\n")
	for line in content:
		aux = aux + 1;
		if line[0] == '#':
			if line.find(GRUPO) > 0:
				content[aux-1] = content[aux-1] + MSG
				achei = achei + 1
		else:
			pass
	if achei == 0:
		#print("GRUPO NÃO ENCONTRADO CRIANDO AGORA !!!\n")
		TXT = "# " + GRUPO + "\n"
		OpenWriteClose(File, TXT)
		OpenWriteClose(File, MSG)
	#print("\n\n CONTENTE DEPOIS", content, "\n\n")
	if achei > 0:
		with open(File, 'w') as f:
			for item in content:
				f.write("{}".format(item))
# IMPLEMENTAR SE CONTATO EXISTIR NÃO ADICIONAR NOVAMENTE
def addCONTATO(File, contato, IP, MSG):
	locate = 0
	print("-------", File)
	with open(File) as f:
		content = f.readlines()
		f.close()
	for line in content:
		locate = line.find(contato)
		if locate > 0:
			print("\nUSUARIO JA EXISTENTE !!!!!!!!!!!!!!!\n")
		else:
			pass
	if locate <= 0:
		print("\n ADICIONANDO USUARIO NA LISTA!!!!")
		with open(File, 'a') as f:
			f.write(MSG)






def addM(file, x):
	pass
def addLE(file, x):
	pass


# IDENTIFICAR OS PRIMEIRO CARACTER DA LINHA QUE IDENTIFICA O ESTADO DA FUNCAO
# RETORNA A PRIMEIRA LINHA ONDE FALTA EXECUTAR 
def FindWORK():
	f = open("listaEspera.txt","r")
	linelist = f.readlines()
	# count = len(linelist)
	# print linelist[input][0]	PASSANDO DOIS PARAMETROS PERCORREMOS A LINHA CARACTER POR CARACTER
