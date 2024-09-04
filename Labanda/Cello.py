from Instrument import Instrument


class Cello(Instrument):
    def __init__(self):
        self.instrument_type = 'Cello'

    def play(self):
        print(f'{self.instrument_type}')
        
    def tune(self):
        print(f'{self.instrument_type}')    
	