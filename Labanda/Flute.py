from Instrument import Instrument


class Flute(Instrument):
    def __init__(self, sound):
         super().__init__(sound) 
         print(f'{sound}')
