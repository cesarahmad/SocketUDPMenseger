import os, sys
import time
from threading import Thread


import UDP_comunication as UDP
import File_WRA as file


listacontatos 	= 'listaUG.txt'
listamensagens 	= 'mensagens.txt'
LOGFILE 		= 'LOG.txt'
worksheet 		= 'worksheet.txt'

mensagemcontatonaoexiste = 'CONTATO NÃO EXISTE !!!'
mensagemcontatoexiste = 'CONTATO JA EXISTE !!!'
mensagemgruponaoexiste = 'GRUPO NAO EXISTE !!!'
errogrupo = 'MULTIPLOS CONTATOS NO GRUPO ---- ERRO 171'
opcaoinvalida = 'OPCAO INVALIDA DIGITE OUTRA OPCAO'
existemultiploscontato = 'EXISTE MULTIPLOS CONTATOS COM MESMO NOME ERRO 312'
naoexistemensagem = 'NAO EXISTE MENSAGENS PARA ESTE CONTATO !!!'

localizounome = 0
localizoumsg = 0

MAX = 100

# VETOR DE OJETOS COM TAMANHO DEFINIDO E SEM DEFINIR TAM
MSG = [UDP.mensagem() for i in [100]]
MSGAUX = UDP.mensagem()
MSGAUXRECV = UDP.mensagem()


def InterfaceUSER_THREAD():
	opcao = '.'
	while opcao != 'T':
		MSGAUX = UDP.mensagem()
		opcao = UDP.display()
		# ********* TALVEZ SEJA NECESSARIO RESETAR MSGAUX
		# NESTE EXEMPLO SO CONFIRO SE NOME EXISTE NÃO O IP ***obs: PODE EXISTIR MULTIPLOS USUARIOS NO MESMO IP
		if opcao == 'i':
			nomecontato = input("Digite o nome do contato: \t")
			if MSGAUX.contatoexiste(listacontatos, nomecontato) == 0:
				ipcontato = input("Digite o numero IP com '.': \t")
				MSGAUX.setnome(nomecontato)
				MSGAUX.setipd(ipcontato)
				MSGAUX.saveMSG(listacontatos)
				MSGAUX.setaux('ADICONANDO CONTATO')
				MSGAUX.saveMSG(LOGFILE)
			else:
				print(mensagemcontatoexiste)
				UDP.saveMSG(LOGFILE, 'ALERTA - CONTATO JA EXISTENTE\n')

		elif opcao == 'g':
			nomegrupo = input("Digite o nome do grupo: \t")
			nomecontato = input("Digite o nome do contato: \t")
			ipcontato = input("Digite o numero IP com '.': \t")

			aux = MSGAUX.grupoexiste(listacontatos, nomecontato, nomegrupo)
			# EXISTE GRUPO MAS NAO CONTATO && NAO EXISTE GRUPO 
			if aux <= 0:
				MSGAUX.setgrupo(nomegrupo)
				MSGAUX.setnome(nomecontato)
				MSGAUX.setipd(ipcontato)
				MSGAUX.saveMSG(listacontatos)
				MSGAUX.setaux('ADICIONANDO CONTATO AO GRUPO')
				MSGAUX.saveMSG(LOGFILE)
			# JA EXISTE CONTATO NO GRUPO
			if aux == 1:
				print("JA EXISTE CONTATO NO GRUPO....")
				UDP.saveMSG(LOGFILE, 'ALERTA - CONTATO JA EXISTENTE NO GRUPO\n')
			# EXISTE MULTIPLOS CONTATOS NO GRUPO
			if aux > 1:
				print(errogrupo)
				UDP.saveMSG(LOGFILE, 'ALERTA - ERRO - FALHA 171 MULTIPLOS CONTATOS NO GRUPO\n')


		##
		### SOLICITAR ANTES SE É USUARIO OU GRUPO
		### SE FOR GRUPO ADD TAREFA NO WORKSHEET PARA A OUTRA THREAD EXECUTAR
		##
		elif opcao == 's':
			UG = input("Digite 'U' - para usuario\nDigite 'G' - para GRUPO\n")
			nome = input("Digite o nome do contato ou grupo para enviar mensagem:\t") 
			aux = MSGAUX.contatoexiste(listacontatos, nome)
			if UG == 'u' and aux == 1:
				msg = input("Digite sua mensagem: \n\t")
				MSGAUX.setnome(nome)
				MSGAUX.setmsg(msg)
				MSGAUX.setstatus('@')
				MSGAUX.saveMSG(listamensagens)
				MSGAUX.enviarMSG()
				MSGAUX.setaux('ADICIONANDO ENVIANDO MENSAGEM')
				MSGAUX.saveMSG(LOGFILE)

			elif UG == 'g':
				####
				## TALVEZ SEJA NECESSARIO SEMAFARO PARA CONTROLE DE ACESSO.
				####
				# SALVAR TAREFA NO WORKSHEET PARA CUMPRIR DEPOIS ADICIONAR MARCADOR PARA IDENTIFICAR TAREFA DE MANDAR PARA O GRUPO
				MSGAUX.saveMSG(worksheet)
			else:
				print(mensagemcontatonaoexiste)
				UDP.saveMSG(LOGFILE, 'ALERTA - CONTATO NAO EXISTENTE\n')

		# PREVER SE TIVER GRUPO COM MESMO NOME QUE CONTATO VAI DAR ERRO.........
		###
		### ACHO QUE ELE NÃO LEVA EM CONSIDERAÇÃO NA HORA DE IMPRIMIR LISTA DE CONTATO & GRUPO QUE NÃO PODERA REPETIR NOMES
		###
		elif opcao == 'l':
			UG = input("Digite 'U' - para usuario\nDigite 'G' - para GRUPO\n")
			nome = input("Digite o nome do contato ou grupo para visualizar mensagens:\t")
			localizounome, localizoumsg = MSGAUX.listarMSG(listacontatos, listamensagens, nome, UG)
			#print("---- ", localizounome, localizoumsg, "\n")
			if localizounome > 1:
				print(existemultiploscontato)
			elif localizounome <= 0:
				print(mensagemcontatonaoexiste)
			elif localizoumsg == 0:
				print(naoexistemensagem)


		elif opcao == 'c':
			MSGAUX.listarContatos(listacontatos)


		elif opcao == 'd':
			pass
		elif opcao == 'H':
			pass
		# TERMINA O PROGRAMA
		elif opcao == 'T':
			UDP.enviarMSG('T')
		else:
			print(opcaoinvalida)


def recev_THREAD():
	RECVTXT = UDP.receberMSG()
	MSGAUXRECV.setRECV(RECVTXT)
	MSGAUXRECV.saveMSG(worksheet)
	MSGAUXRECV.setaux('MSG RECEBIDA E SALVA NO WORKSHEET.TXT')
	####
	## TALVEZ SEJA NECESSARIO SEMAFARO PARA CONTROLE DE ACESSO.
	####
	MSGAUXRECV.saveMSG(worksheet)
	if MSGAUXRECV == 'T':
		return 0

def worksheet_THREADS():
	pass

# MAIN () ******************************************************************


t1 = Thread(target = InterfaceUSER_THREAD)
t2 = Thread(target = recev_THREAD)
t3 = Thread(target = worksheet_THREADS)

t1.start()
t2.start()
t3.start()

#t1.join()
#t2.join()
#t3.join()
