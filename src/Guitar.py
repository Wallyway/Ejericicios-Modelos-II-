from Instrument import Instrument


class Guitar(Instrument):
	def play(self):
		print(f"Guitar PLaying {self.sound} and {self.type}") 