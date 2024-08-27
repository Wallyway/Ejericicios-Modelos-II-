class Musician:
	def __init__(self, instrument, name):
		self.instrument = instrument
		self.name = name
	
	def tune(self):
		print(self.name,"is tuning his instrument.")
	
	def play(self):
		print(self.name,"is playing")
		