import random


class Unit:
    def __init__(self, name, clan, _health=100, _strength=10, _agility=10, _intellect=10):
        self.name = name
        self.clan = clan
        self.health = _health
        self.strength = _strength
        self.agility = _agility
        self.intellect = _intellect

    def _health(self):
        self.health = random.randrange(1, 101)
        print(self.health)
        return self.health

    def _strength(self):
        self.strength = random.randrange(1, 101)
        print(self.strength)
        return self.strength

    def _agility(self):
        self.agility = random.randrange(1, 101)
        print(self.agility)
        return self.agility

    def _intellect(self):
        self.intellect = random.randrange(1, 101)
        print(self.intellect)
        return self.intellect

    def _recovery_health(self):
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
        print(self.health)
        return self.health


class Mage(Unit):
    def __init__(self, name, clan, type_magic):
        super().__init__(name, clan)
        self.type_magic = type_magic
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intellect = self._intellect()

    def recuperation_intellect(self):
        if self.intellect <= 9:
            self.intellect += 1
        else:
            self.intellect = 10
        print(self.intellect)
        return self.intellect


Unit_mage = Mage("Дамблдор", "Люди", "Воздух")
print(f'{Unit_mage.name} клан {Unit_mage.clan}, дополнительная характеристика {Unit_mage.type_magic}. Здоровье : {Unit_mage.health}, сила: {Unit_mage.strength}, ловкость: {Unit_mage.agility}, интеллект: {Unit_mage.intellect}.')
