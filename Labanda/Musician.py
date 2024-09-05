import random
from Instrument import Instrument
from InstrumentFactory import InstrumentFactory


class Musician:
    def __init__(self, name, instrument: Instrument):
        self.name = name
        self.instrument = instrument

    def play(self):
        print(self.name,"esta tocando...")
        self.instrument.play()

    def tune(self):
        print(self.name,"esta afinando...")

