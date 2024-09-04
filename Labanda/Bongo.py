from Instrument import Instrument


class Bongo(Instrument):
    def __init__(self):
        self.instrument_type = 'Bongoes'

    def play(self):
        print(f'{self.instrument_type}')
        
    def tune(self):
        print(f'{self.instrument_type}')    
	