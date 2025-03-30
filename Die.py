import random

class Die:
    def __init__(self):
        self.roll=0

    def rollDie(self):
        self.roll=random.randint(1,6)
    

die=Die()
print(die.rollDie())