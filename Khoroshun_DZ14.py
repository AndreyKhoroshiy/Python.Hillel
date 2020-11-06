import random


class Unit:
    def __init__(self, name, clan, _health=100, _strength=10, _agility=10, _intellect=10):
        self.name = name
        self.clan = clan
        self.health = _health
        self.strenght = _strength
        self.agility = _agility
        self.intellect = _intellect

    def _health(self):
        self.health = random.randrange(1, 101)
        print(self.health)
        return self.health

    def _strength(self):
        self.strenght = random.randrange(1, 101)
        print(self.strenght)
        return self.strenght

    def _agility(self):
        self.agility = random.randrange(1, 101)
        print(self.agility)
        return self.agility

    def _intellect(self):
        self.intellect = random.randrange(1, 101)
        print(self.intellect)
        return self.intellect

    def _recovery(self):
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
        print(self.health)
        return self.health


class Mage(Unit):
    def __init__(self, name, clan, type_magic):
        super().__init__(name, clan)

