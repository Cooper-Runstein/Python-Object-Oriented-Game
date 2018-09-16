import arcade


class BoardGUI:
    def __init__(self, tiles):
        self.tile_types = [
            {'terrain_name': 'ocean'},
            {'terrain_name': 'ocean'},
            {'terrain_name': 'desert'},
            {'terrain_name': 'mountains'},
            {'terrain_name': 'desert'},
            {'terrain_name': 'plains'},

        ]

        self.colors = {
            'green': arcade.color.GREEN,
            'yellow': arcade.color.YELLOW,
            'black': arcade.color.BLACK,
            'grey': arcade.color.GRAY,
            'blue': arcade.color.BLUE,

        }

        self.draw_terrains_funcs = {
            'ocean': self.draw_ocean,
            'mountains': self.draw_mountains,
            'desert': self.draw_desert,
            'plains': self.draw_plains
        }

        self.TILE_SIZE = 20

        arcade.open_window(600, 600, "Example")
        arcade.set_background_color(arcade.color.WHITE)
        arcade.start_render()

        self.x_pos = 10
        self.y_pos = 0
        for tile in tiles:
            self.draw_terrains_funcs[tile['terrain_name']](self.x_pos, self.y_pos)
            print(tile['terrain_name'])
            self.x_pos += 10

        arcade.finish_render()
        arcade.run()

    def draw_terrain(self, x_pos, y_pos, color):
        arcade.draw_rectangle_filled(x_pos, y_pos, self.TILE_SIZE, self.TILE_SIZE, color)

    def draw_plains(self, x_pos, y_pos):
        self.draw_terrain(x_pos, y_pos, self.colors['green'])

    def draw_desert(self, x_pos, y_pos):
        self.draw_terrain(x_pos, y_pos, self.colors['yellow'])

    def draw_mountains(self, x_pos, y_pos):
        self.draw_terrain(x_pos, y_pos, self.colors['grey'])

    def draw_ocean(self, x_pos, y_pos):
        self.draw_terrain(x_pos, y_pos, self.colors['blue'])

my_board = BoardGUI([{'terrain_name': 'ocean'}])

