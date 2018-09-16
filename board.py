import random
class Board():
    def __init__(self, side_length):
        self.side_length = side_length
        self.board_size = side_length * side_length
        self.board = self.initialize_board()


    def create_tile(self, cords):
        ''' Create and return a random tile object'''
        terain_id = random.randint(0, 5)
        terain_names = {
            0: Tile.create_hills,
            1: Tile.create_ocean,
            2: Tile.create_desert,
            3: Tile.create_forest,
            4: Tile.create_plains,
            5: Tile.create_mountains
        }
        tile = terain_names[terain_id]((cords))
        return tile


    def initialize_board(self):
        '''initialize the board with a set of tiles'''
        board = []
        for x_cord in range(0, self.side_length):
            row = []
            for y_cord in range(0, self.side_length):
                cords = x_cord, y_cord
                row.append(self.create_tile(cords))

            board.append(row)

        return board


    def __repr__(self):
        board = ''
        for x in self.board:
            row = ''
            for y in x:
                row += '{}, '.format(str(y))
            board += row + '\n'

        return board




class Tile():
    def __init__(self, cords, values, owner=None):
        self.cords = cords
        self.food = values['food']
        self.terain_name = values['terain_name']
        self.height = values['height']
        self.owner = owner

    def __repr__(self):
        return '{}: {}'.format(self.cords, self.terain_name)

    @classmethod
    def create_plains(cls, cords):
        '''Create a plains tile'''
        values = {'food': 3, 'height': 1, 'terain_name': 'plains'}
        return cls(cords, values)

    @classmethod
    def create_mountains(cls, cords):
        '''Create a mountain tile'''
        values = {'food': 0, 'height': 3, 'terain_name': 'mountains'}
        return cls(cords, values)

    @classmethod
    def create_desert(cls, cords):
        '''Create a desert tile'''
        values = {'food': 0, 'height': 1, 'terain_name': 'desert'}
        return cls(cords, values)

    @classmethod
    def create_forest(cls, cords):
        '''Create a forest tile'''
        values = {'food': 2, 'height': 1, 'terain_name': 'forest'}
        return cls(cords, values)

    @classmethod
    def create_ocean(cls, cords):
        '''Create an ocean tile'''
        values = {'food': 2, 'height': 0, 'terain_name': 'ocean'}
        return cls(cords, values)


    @classmethod
    def create_hills(cls, cords):
        '''Create a hills tile'''
        values = {'food': 1, 'height': 2, 'terain_name': 'hills'}
        return cls(cords, values)







s = Board(5)
print(s)
