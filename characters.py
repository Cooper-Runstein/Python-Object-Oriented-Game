import random

class Character():
    """docstring forCharacter."""
    def __init__(self, values, **kwargs):
        for attribute, value in kwargs.items():
            setattr(self, attribute, value)

        self.name = values['name']

        self.id = random.randint(0, 10000000000)

        try:
            self.hp = values['hp']
            self.atk = values['atk']
            self.deff = values['def']
        except KeyError:
            pass

        self.fortified = False


    def __repr__(self):
        return '{}: hp:{}, atk:{}, deff:{}'.format(self.name, self.hp, self.atk, self.deff)

    def attack(self, other):
        def get_damage_done(self, other):
            if other.fortified:
                return self.atk - (other.deff + 1)
            damage_done = self.atk - other.deff
            if  damage_done > 1:
                return damage_done
            else:
                return 1

        other.hp -= get_damage_done(self, other)

        damage_returned = self.deff - other.deff

        if damage_returned > 0:
            self.hp -= damage_returned

    def fortify(self):
        self.fortified = True

class Peasant(Character):
    def __init__(self, values, **kwargs):
        super().__init__(values, **kwargs)
        self.hp = 10
        self.atk = 1
        self.deff = 1

class Warrior(Character):
    def __init__(self, values, **kwargs):
        super().__init__(values, **kwargs)
        self.hp = 10
        self.atk = 2
        self.deff = 2

class Catapult(Character):
    def __init__(self, values, **kwargs):
        super().__init__(values, **kwargs)
        self.hp = 10
        self.atk = 3
        self.deff = 0

# base_char = Character({'name': 'Bob', 'hp': 10, 'atk': 8, 'def': 4 })
# secondary_char = Warrior({'name': 'Fred', 'hp': 10, 'atk': 5, 'def': 3})
# peasant = Peasant({'name': 'Sam', 'hp': 10, 'atk': 5, 'def': 3})

# print(base_char)
# print(secondary_char)
# print(peasant)

# base_char.attack(secondary_char)
#
# print(base_char)
# print(secondary_char)
#
# secondary_char.fortify()
# base_char.attack(secondary_char)
#
# print(base_char)
# print(secondary_char)
