from Instrument import Instrument


class Piano(Instrument):
    def __init__(self):
        self.instrument_type = 'Piano'

    def play(self):
        print(f'{self.instrument_type}')
        
    def tune(self):
        print(f'{self.instrument_type}')    
	