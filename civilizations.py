import characters

class Civilization():
    def __init__(self, name, id, units, territory):
        self.name = name
        self.units = units
        self.territory = territory
        self.id = id

    def __repr__(self):
        units_string = ''
        for id, unit in self.units.items():
            units_string += '{}, '.format(str(unit.name))
        return '{}: {}'.format(self.name, units_string)

    def add_unit(self, unit):
        self.units[unit.id] = unit
        assert self.units[unit.id] == unit

    def remove_unit(self, unit):
        del self.units[unit.id]

    def add_territory(cords):
        for x in cords:
            pass





c = Civilization('team1', {})
unit = characters.Warrior({'name': 'Jim',})
c.add_unit(unit)
print(c)
c.remove_unit(unit)
print(c)
