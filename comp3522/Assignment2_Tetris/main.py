from game import Game
from tetrominos import BasicTetrominoFactory

def main():
    factory = BasicTetrominoFactory()
    game = Game(factory)
    game.run()

if __name__ == '__main__':
    main()