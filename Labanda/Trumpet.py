from Instrument import Instrument


class Trumpet(Instrument):
    def __init__(self, sound):
        super().__init__(sound)
        print(f'{sound}')

