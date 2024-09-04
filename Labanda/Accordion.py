from Instrument import Instrument


class Accordion(Instrument):

    def __init__(self, sound) -> None:
        super().__init__(sound)
        print(f'{sound}')


