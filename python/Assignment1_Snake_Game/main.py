from game import Game, GameBoard

"""Snake Game Main Module

This module contains the main function to run the Snake game.
It initializes the game board and the game itself, then runs the game loop.

"""


def main():
    """Main function to run the Snake game."""
    # initialize the game board
    game_board = GameBoard(800, 800)

    # initialize the game
    game = Game(game_board)

    # run the game
    game.run_game()


if __name__ == "__main__":
    main()
