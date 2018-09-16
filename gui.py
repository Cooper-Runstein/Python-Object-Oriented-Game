import arcade


class BoardGUI:
    def __init__(self, tiles):
        self.tiles = tiles
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
            'purple': arcade.color.PURPLE,
            'dark-green': arcade.color.DARK_GREEN

        }

        self.draw_terrains_funcs = {
            'ocean': self.draw_ocean,
            'mountains': self.draw_mountains,
            'desert': self.draw_desert,
            'plains': self.draw_plains,
            'hills': self.draw_hills,
            'forest': self.draw_forest,
        }

        self.TILE_SIZE = 40

        arcade.open_window(600, 600, "Example")
        arcade.set_background_color(arcade.color.WHITE)
        arcade.start_render()

        self.run_render(tiles)

        arcade.finish_render()
        arcade.run()

    def run_render(self, tiles):
        """Run the game drawings"""
        x_pos = 20
        y_pos = 20
        for row in tiles:
            for tile in row:
                self.draw_terrains_funcs[tile.terrain_name](x_pos, y_pos)
                # print(tile['terrain_name'])
                x_pos += self.TILE_SIZE
            y_pos += self.TILE_SIZE
            x_pos = 20

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

    def draw_hills(self, x_pos, y_pos):
        self.draw_terrain(x_pos, y_pos, self.colors['purple'])

    def draw_forest(self, x_pos, y_pos):
        self.draw_terrain(x_pos, y_pos, self.colors['dark-green'])

    def __repr__(self):
        return 'BoardGUI: {}'.format(*self.tiles)

if __name__ == "__main__":
    my_board = BoardGUI([{'terrain_name': 'ocean'}])