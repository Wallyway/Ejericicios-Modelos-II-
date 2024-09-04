import random
from InstrumentCreator import InstrumentCreator


class Musician:
    def __init__(self, name, instrument: Instrument):
        self.name = name
        self.instrument = instrument

    def play(self):
        print(f'{self.name} esta tocando...', end=' ')
        self.instrument.play()

    def tune(self):
        print(f'{self.name} esta afinando...', end=' ')
        self.instrument.tune()

