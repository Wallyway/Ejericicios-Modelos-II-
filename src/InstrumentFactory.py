import random

from Guitar import Guitar
from Drums import Drums
from Instrument import Instrument

class InstrumentFactory:
	def get_random(self):
		randint = random.randint(1, 2)
		if randint == 1:
			return Guitar(sound="strumming", type="Acoustica")
		if randint==2:
			return Drums(sound="percusion", type="Drum kit")