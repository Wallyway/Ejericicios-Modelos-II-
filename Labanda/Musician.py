


import random
from InstrumentCreator import InstrumentCreator


class Musician:
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def play(self):
        print(f'{self.name} esta tocando', end=' ')
        self.instrument.play()

    def tune(self):
        print(f'{self.name} esta afinando', end=' ')
        self.instrument.tune()

def generate_random_names(num_names):
    names = ['Juan', 'Andres', 'Laura', 'David', 'Santiago', 'Pedro', 'Martin', 'Ana', 'Ivan', 'Julia']
    random.shuffle(names)   #Aqui se evita repeticion de nombres por barjacion
    return names[:num_names]

def create_random_musicians(num_musicians):
    names = generate_random_names(num_musicians)
    instrument_creator = InstrumentCreator()
    return [Musician(name, instrument_creator.create_instrument()) for name in names]