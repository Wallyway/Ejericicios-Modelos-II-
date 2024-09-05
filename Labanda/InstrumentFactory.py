import random
from Accordion import Accordion
from Guitar import Guitar
from Instrument import Instrument
from Guitarron import Guitarron
from Harp import Harp
from Trombone import Trombone
from Trumpet import Trumpet
from Vihuela import Vihuela
from Maracas import Maracas
from Violin import Violin
from Flute import Flute


class InstrumentFactory:
    
    def random(self):
        rand = random.randint(1,10)
        instrument = None
        if rand== 1:
            instrument = Accordion("Accordion sound")
        elif rand == 2:
            instrument = Vihuela("Vihuela sound")
        elif rand== 3:
            instrument = Trumpet("Trumped sound")
        elif rand == 4:
            instrument = Guitar("Guitar sound")
        elif rand == 5:
            instrument = Maracas("Maracas sound")
        elif rand == 6:
            instrument = Guitarron("Guitarron sound")
        elif rand == 7:
            instrument = Violin("Violin sound")
        elif rand == 8:
            instrument = Trombone("Trombone sound")
        elif rand == 9:
            instrument = Harp("Harp sound")
        elif rand == 10:
            instrument = Flute("Flute sound")
        else:
            instrument = Instrument("Unknown")
        return instrument
	
     
