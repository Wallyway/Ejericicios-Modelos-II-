import random

from Musician import Musician
from InstrumentFactory import InstrumentFactory


class Band:
	def __init__(self):
		self.musicians = []

	def play(self):
		for musician in self.musicians:
			musician.play()

	def tune(self):
		for musician in self.musicians:
				musician.tune()

	def random(self):
		rand_musicians = random.randint(1,10)
		instrumentf = InstrumentFactory()	
		names = ['Juan', 'Andres', 'Laura', 'David', 'Santiago', 'Pedro', 'Martin', 'Ana', 'Ivan', 'Julia']
		random.shuffle(names)   #Aqui se evita repeticion de nombres por barjacion
		names = names[:rand_musicians]
		for n in names:
			self.musicians.append(Musician(n, instrumentf.random()))

