from Instrument import Instrument


class Maracas(Instrument):
    def __init__(self):
        self.instrument_type = 'Maraca'

    def play(self):
        print(f'{self.instrument_type}')
        
    def tune(self):
        print(f'{self.instrument_type}')    
	