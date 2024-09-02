
class Musician:
	def __init__(self, name, instrument):
		self.instrument = instrument
		self.name = name
	
	def tune(self):
		print(self.name,"is tuning his instrument.")
	
	def play(self):
		print(f"{self.name} is playing {self.instrument}")
		