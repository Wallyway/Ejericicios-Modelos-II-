import random
from Accordion import Accordion
from Bongo import Bongo
from Cello import Cello
from Drums import Drums
from Guitar import Guitar
from Instrument import Instrument
from Maracas import Maracas
from Piano import Piano
from Trumped import Trumped
from Violin import Violin
from Violing import Violing

class InstrumentCreator:
    def __init__(self):
        self.available_instruments = [Accordion(),Bongo(),Cello(), Drums(),Guitar(),Maracas(),Piano(),Trumped(),Violin(),Violing()]  # Add more instruments here

    def create_instrument(self):
        if not self.available_instruments:
            raise ValueError("No available instruments")
        return self.available_instruments.pop(random.randint(0, len(self.available_instruments) - 1))
