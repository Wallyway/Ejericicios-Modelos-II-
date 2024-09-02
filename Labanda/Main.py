
import random
from Band import Band
from Musician import create_random_musicians


class Main:
    def run(self):
        num_musicians = random.randint(5,10)
        musicians = create_random_musicians(num_musicians)
        chisga = Band(musicians)
        print("------------AFINANDO-----------\n")
        chisga.tune()
        print("------------TOCANDO-----------\n")
        chisga.play()

if __name__ == "__main__":
    Main().run()