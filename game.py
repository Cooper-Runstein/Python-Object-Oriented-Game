import characters
import civilizations
import board




def main():
    try:
        game = define_board()
        print(game.board_size)
    except ValueError:
        print('Please retry.')
        main()


def define_board():
    get_board_size = input('Select a size, s/M/l, or custom size')
    try:
        board_size = int(get_board_size)
    except ValueError:
        if get_board_size.lower() == 's':
            board_size = 10
        elif get_board_size.lower() == 'l':
            board_size = 25
        else:
            board_size = 18

    if 5 < board_size < 40:
        game = board.Board(board_size)
        return game

    else:
        raise ValueError ('Bad board size')

main()