from Instrument import Instrument

class Drums(Instrument):
    def __init__(self):
        self.instrument_type = 'Bateria'
        self.sound = 'Acustica'

    def play(self):
        print(f'{self.instrument_type}')
        
    def tune(self):
        print(f'{self.instrument_type}')