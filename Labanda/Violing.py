from Instrument import Instrument


class Violing(Instrument):
    def __init__(self):
        self.instrument_type = 'Viola'
        

    def play(self):
        print(f'{self.instrument_type}')
        
    def tune(self):
        print(f'{self.instrument_type}') 