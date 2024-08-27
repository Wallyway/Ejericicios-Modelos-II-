import random

from Guitar import Guitar

class InstrumentFactory:
	def get_radom(self):
		randint = random.randint(1, 6)
		if randint == 1:
			return Guitar()