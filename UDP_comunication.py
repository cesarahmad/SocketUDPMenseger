import os, sys
import time

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

	def __set__(self, ID, IPO, IPD, PortO, PortD, MSG):
		self.ID = ID
		self.ipo = IPO
		self.ipd = IPD
		self.porto = PortO
		self.portd = PortD
		self.MSG = MSG

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

	def getid(self):
		return self.ID
	def getipo(self):
		return self.ipo
	def getipd(self):
		return self.ipo
	def getporto(self):
		return self.porto
	def getportd(self):
		return self.portd
	def getmsg(self):
		return self.MSG



	def teste(self):
		print("DENTRO DA CLASS MENSAGEM")

def teste():
	print("FORA DA CLASS MENSAGEM")
	





