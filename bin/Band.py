from enum import member
import random
from InstrumentFactory import InstrumentFactory
from Musician import Musician

class Band:
	def __init__(self, name):
		self.name = name
		self.members = []
	
	def play(self):
		for member in self.members:
			member.play()
	
	def tune(self):
		for member in self.members:
			member.tune()

	def add_member(self, musician):
		self.members.append(musician)

	
	def random(self):
		names = ["Carina", "Laura", "Jonathan", "Fernando", "David", "Elisa", "Camilo", "Daniel", "Jacob", "Emir", "Maria"]
		for i in range(6):
			name= names[i]
			instrument= InstrumentFactory().get_random()
			musician = Musician(name=name, instrument=instrument)
			self.add_member(musician)
 		

my_band = Band(name="Awesome Band")
my_band.random()
my_band.tune()
my_band.play()