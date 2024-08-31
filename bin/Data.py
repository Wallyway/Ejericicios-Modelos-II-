

class Data:
	def __init__(self):
		self.raw = []
	
	def random(self):
		return self.raw[random.randint(0, len(self.raw)-1)]