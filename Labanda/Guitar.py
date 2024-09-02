
from Instrument import Instrument


class Guitar(Instrument):
    def __init__(self):
        self.instrument_type = 'Guitarra'

    def play(self):
        print(f'{self.instrument_type}')

    def tune(self):
        print(f'{self.instrument_type}')