import os, sys
import time

import UDP_comunication as UDP
import File_WRA as file


listacontatos 	= 'listaUG.txt'
listamensagens 	= 'mensagens.txt'
LOGFILE 		= 'LOG.txt'

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


opcao = UDP.display()


# NESTE EXEMPLO SO CONFIRO SE NOME EXISTE NÃO O IP ***obs: PODE EXISTIR MULTIPLOS USUARIOS NO MESMO IP
if opcao == 'i':
	nomecontato = input("Digite o nome do contato: \t")
	ipcontato = input("Digite o numero IP com '.': \t")
	if MSGAUX.contatoexiste(listacontatos, nomecontato) == 0:
		MSGAUX.setnome(nomecontato)
		MSGAUX.setipd(ipcontato)
		MSGAUX.saveMSG(listacontatos)
	else:
		print(mensagemcontatoexiste)

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
	# JA EXISTE CONTATO NO GRUPO
	if aux == 1:
		print("JA EXISTE CONTATO NO GRUPO....")
	# EXISTE MULTIPLOS CONTATOS NO GRUPO
	if aux > 1:
		print(errogrupo)



# PREVER SE TIVER GRUPO COM MESMO NOME QUE CONTATO VAI DAR ERRO.........
###
### ACHO QUE ELE NÃO LEVA EM CONSIDERAÇÃO NA HORA DE IMPRIMIR LISTA DE CONTATO & GRUPO QUE NÃO PODERA REPETIR NOMES
###
elif opcao == 'l':
	nome = input("Digite o nome do contato ou grupo para visualizar mensagens:\t")
	localizounome, localizoumsg = MSGAUX.listarMSG(listacontatos, listamensagens, nome)
	#print("---- ", localizounome, localizoumsg, "\n")
	if localizounome > 1:
		print(existemultiploscontato)
	elif localizounome <= 0:
		print(mensagemcontatonaoexiste)
	elif localizoumsg == 0:
		print(naoexistemensagem)

elif opcao == 's':
	nome = input("Digite o nome do contato ou grupo para enviar mensagem:\t") 
	msg = input("Digite sua mensagem: \n\t")
	if contatoexiste(listacontatos, nome) == 1:
		MSGAUX.setnome(nome)
		MSGAUX.setmsg(msg)
		MSGAUX.enviarMSG()
	else:
		print(mensagemcontatonaoexiste)

elif opcao == 'c':
	MSGAUX.listarContatos(listacontatos)


elif opcao == 'd':
	pass
elif opcao == 'H':
	pass


else:
	print(opcaoinvalida)