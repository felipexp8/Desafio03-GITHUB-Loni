# coding: utf-8

import random as rnd

class Operador:

	"""
	Percorre toda a String fornecida no parametro input
	"""

	
	def doA(self, pos):	
		if type(pos)!=int: return
		self.S+= self.origem[pos]
		self.resultado+=self.A
		self.score["A"]+=1
		return 1
		
	def doB(self,inicio,fim):
		if type(inicio+fim)!=int: return
		self.S+=self.S[inicio:fim]
		self.resultado+=self.B
		self.score["B"]+=1
	
	def reset(self):
		self.resultado = 0
		self.score = {"A":0 , "B":0}
	
	def __init__(self, input = "zzz", A = 1, B = 1):
		
		self.S = str()
		
		self.A = A
		self.B = B
		self.origem = input
		
		self.tamanho = len(input)
		
		self.resultado = 0
    
		self.score = {"A":0 , "B":0}
		
		self.listaResultado = []
		
	def pre(self): #inicia a self.S com os primeiros valores de Input
		self.doA(0)
		self.doA(1)
		
	
	
	def monteCarlo(self, repeticao):
	
		for x in range(repeticao):
		
			self.reset()
	
			self.pre()
			
			itera = 0;
			
			while(itera<self.tamanho):
			
				itera += self.detectaExa(itera)*rnd.choice([1, 0])
				if(itera>=self.tamanho): return
				itera += self.detectaQuadra(itera)*rnd.choice([1, 0])
				if(itera>=self.tamanho): return
				itera += self.doA(itera)
				
			self.listaResultado.append(self.resultado)
		

	
	def monta(self):
		 
		self.reset()
		
		
		self.pre()
		
		itera = 0;
		
		if self.B < self.A: #nao é ótimo, mas para string grandes converge nisto:
			while(itera<self.tamanho):
				itera += self.detectaExa(itera)
				if(itera>=self.tamanho): return
				itera += self.detectaQuadra(itera)
				if(itera>=self.tamanho): return
				itera += self.doA(itera)
		else:
			while(itera<self.tamanho):			 
				itera += self.doA(itera)
			
	def detectaQuadra(self,pos):
		if self.S[pos-2:pos] == self.S[pos:pos+2]:
			self.doB(pos-2,pos)
			return 2
		else:
			return 0
		
	def detectaExa(self,pos):
		if self.S[pos-3:pos] == self.S[pos:pos+3]:
			self.doB(pos-3,pos)
			return 3
		else:
			return 0	
		

rnd.seed(12345)

fornecedor = Operador("abcdurgfer",6,1)

fornecedor.monta()

print(fornecedor.resultado)
print(fornecedor.S) 

fornecedor2 = Operador("aaaauauaaer",6,1)

fornecedor2.monta()

print(fornecedor2.resultado)
print(fornecedor2.S)   

fornecedor2.monteCarlo(1000)

print("forcando melhor caminho: MonteCarlo:")

print(min(fornecedor2.listaResultado)) 

