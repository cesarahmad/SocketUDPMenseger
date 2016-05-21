#! usr/bin/python

import os, sys
import socket
import time

import fileinput

import whatsappLIB as whats


def atendimentoF(arg):
	# Inserir contato
	## SE EXISTIR NÃO ADD $$$$$$$$$
	### ADD LOG MESSAGE
	if   arg == 'i':
		nomeU = input("Digite o nome Usuario !\t")
		IPU = input("Digite o numero IP com '.'' !\t")
		MSG = nomeU + '\t' + IPU + '\n'
		#OpenWriteClose('listaUG.txt', MSG)
		whats.addCONTATO('listaUG.txt', nomeU, IPU, MSG)
		
	# Insere usuario em Grupo
	## SE EXISTIR NÃO ADD $$$$$$$$$
	### ADD LOG MESSAGE
	elif arg == 'g':
		nomeG = input("Digite o nome do GRUPO !\t")
		nomeU = input("Digite o nome Usuario !\t")
		IPU = input("Digite o numero IP com do USUARIO'.'' !\t")
		MSG = '\t' + nomeU + '\t' + IPU + '\n'
		#OpenWriteClose('listaUG.txt', str(MSG))
		whats.addGRUPO('listaUG.txt', nomeG, MSG)

	# Lista as mensagens do Usuario ou Grupo com o estatos no final da mensagem
	## FALTA IMPLEMENTAR DISPLAYM(FILE, USUARIO/GRUPO)
	### ADD LOG MESSAGE
	elif arg == 'l':
		nome = input("Digite o NOME de usuario ou GRUPO para visualizar Mensagens!\t")
		whats.displayM('listaM.txt', str(nome))

	# Envia uma mensagem para um Usuario ou Grupo
	## '+' - TENTANDO ENVIAR     '*' - ENVIADO     '$' - RECEBIDO     '@' - LIDO
	### ADD LOG MESSAGE
	elif arg == 's':
		nome = input("Digite o NOME de usuario ou GRUPO para enviar Mensagen!\t")
		mensagem = input("Digite sua mensagem!\t")
		status = '+'
		if nome == 'termino':
			MSG = 'termino'
			whats.enviarM(str(MSG))
		else:
			MSG = nome + '\t' + mensagem + '\t' + status + '\n'
			whats.enviarM(str(MSG))
			whats.OpenWriteClose('listaM.txt', MSG)

	# Lista todos os Contatos e Grupos
	##
	### ADD LOG MESSAGE
	elif arg == 'c':
		Fileprint('listaUG.txt')

	# Deletar um CONTATO ou GRUPO
	##
	### ADD LOG MESSAGE
	elif arg == 'd':
		pass
	
	# HELP !!!
	##
	### ADD LOG MESSAGE
	elif arg == 'H':
		pass

	##
	### ADD LOG MESSAGE
	else:
		print('NAO EXISTE ESSA OPCAO')
		return 0
	


def Verf_Usuario():
	pass

def child():
	MSG_RECEBIDO = ''
	while MSG_RECEBIDO != "termino":
		MSG_RECEBIDO = whats.receberM()
	print("\n\nCHILD KILLED - PROCESSO DE RECEPCAO ***********\n\n")

def parent():
	newpid = os.fork()
	if newpid == 0:
		child()
	else:
		main()


def main():
	val = ''
	while val != '.':
		whats.displayF()
		time.sleep(1)
		val = input("Digite uma opcao:      \t")
		#time.sleep(1)
		atendimentoF(str(val))


parent()