from Instrument import Instrument


class Trumped(Instrument):
    def __init__(self):
        self.instrument_type = 'Trompeta'
       

    def play(self):
        print(f'{self.instrument_type}')
        
    def tune(self):
        print(f'{self.instrument_type}') 