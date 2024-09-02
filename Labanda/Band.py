


class Band:
    def __init__(self, musicians):
        self.musicians = musicians

    def play(self):
        for musician in self.musicians:
            musician.play()
            print()

    def tune(self):
        for musician in self.musicians:
            musician.tune()
            print() 