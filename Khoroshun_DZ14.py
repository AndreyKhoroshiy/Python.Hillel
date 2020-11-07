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


Unit_mage = Mage("Дамблдор", "Люди", "Воздух")
print(f'{Unit_mage.name} клан {Unit_mage.clan}, дополнительная характеристика {Unit_mage.type_magic}. Здоровье : {Unit_mage.health}, сила: {Unit_mage.strength}, ловкость: {Unit_mage.agility}, интеллект: {Unit_mage.intellect}.')


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


Unit_archer = Archer("Леголас", "Эльф", "Лук")
print(f'{Unit_archer.name} клан {Unit_archer.clan}, дополнительная характеристика {Unit_archer.type_bow}. Здоровье : {Unit_archer.health}, сила: {Unit_archer.strength}, ловкость: {Unit_archer.agility}, интеллект: {Unit_archer.intellect}.')


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


Unit_Knight = Knight("Ланцелот", "Человек", "Меч")
print(f'{Unit_Knight.name} клан {Unit_Knight.clan}, дополнительная характеристика {Unit_Knight.type_weapon}. Здоровье : {Unit_Knight.health}, сила: {Unit_Knight.strength}, ловкость: {Unit_Knight.agility}, интеллект: {Unit_Knight.intellect}.')
