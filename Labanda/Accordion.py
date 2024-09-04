from Instrument import Instrument


class Accordion(Instrument):
    def __init__(self):
        self.instrument_type = 'Acordion'

    def play(self):
        print(f'{self.instrument_type}')
        
    def tune(self):
        print(f'{self.instrument_type}')    
	