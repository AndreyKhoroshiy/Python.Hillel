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
        return self.health

    def _strength(self):
        self.strength = random.randrange(1, 11)
        return self.strength

    def _agility(self):
        self.agility = random.randrange(1, 11)
        return self.agility

    def _intellect(self):
        self.intellect = random.randrange(1, 11)
        return self.intellect

    def _recovery_health(self):
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
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
        return self.intellect

    def __repr__(self):
        return f'{self.name} клан {self.clan}, дополнительная характеристика {self.type_magic}. Здоровье : {self.health}, сила: {self.strength}, ловкость: {self.agility}, интеллект: {self.intellect}.'


class Archer(Unit):
    def __init__(self, name, clan, type_bow):
        super().__init__(name, clan)
        self.type_bow = type_bow
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intellect = self._intellect()

    def recuperation_agility(self):
        if self.agility <= 9:
            self.agility += 1
        else:
            self.agility = 10
        return self.agility

    def __repr__(self):
        return f'{self.name} клан {self.clan}, дополнительная характеристика {self.type_bow}. Здоровье : {self.health}, сила: {self.strength}, ловкость: {self.agility}, интеллект: {self.intellect}.'


class Knight(Unit):

    def __init__(self, name, clan, type_weapon):
        super().__init__(name, clan)
        self.type_weapon = type_weapon
        self.health = self._health()
        self.strength = self._strength()
        self.agility = self._agility()
        self.intellect = self._intellect()

    def recuperation_strength(self):
        if self.strength <= 9:
            self.strength += 1
        else:
            self.strength = 10
        return self.strength

    def __repr__(self):
        return f'{self.name} клан {self.clan}, дополнительная характеристика {self.type_weapon}. Здоровье : {self.health}, сила: {self.strength}, ловкость: {self.agility}, интеллект: {self.intellect}.'


Unit_mage = Mage("Дамблдор", "Люди", "Воздух")
Unit_archer = Archer("Леголас", "Эльф", "Лук")
Unit_Knight = Knight("Ланцелот", "Человек", "Меч")

print(Unit_mage)
print(Unit_archer)
print(Unit_Knight)
