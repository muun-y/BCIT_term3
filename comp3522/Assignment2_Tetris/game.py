import random
import pygame
from command import Command
from grid import Grid
from resources.ui import UI
from tetrominos import (
    ITetromino,
    OTetromino,
    ZTetromino,
    TTetromino,
    STetromino,
    JTetromino,
    LTetromino,
    BasicTetrominoFactory, 
    FreezePowerupTetrominoFactory,
    BombBlockTetrominoFactory,
    TetrominoFactory
)

class Game:
    """Class representing the Tetris game."""

    def __init__(self, factory: TetrominoFactory) -> None:
        """Initialize the game instance.

        Args:
            factory (TetrominoFactory): The factory to create tetrominoes.
        """
        pygame.init()
        self.screen = pygame.display.set_mode((500, 620))
        self.game_over = False
        self.score = 0

        self.grid = Grid()
        self.tetromino = self.spawn_new_tetromino()
        self.factory = BasicTetrominoFactory()
        
        self.ui = UI()
        self.next_tetromino = self.spawn_new_tetromino()

    def run(self):
        """Run the game loop."""
        event_every_200ms = pygame.USEREVENT + 1
        pygame.time.set_timer(event_every_200ms, 200)

        while True:
            command = None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    # Handle keyboard events
                    if event.key == pygame.K_SPACE and self.game_over == True:
                        self.__init__()
                    if event.key == pygame.K_LEFT and self.game_over == False:
                        command = Command.LEFT
                    if event.key == pygame.K_RIGHT and self.game_over == False:
                        command = Command.RIGHT
                    if event.key == pygame.K_f and self.game_over == False:
                        command = Command.F
                        self.factory = FreezePowerupTetrominoFactory()
                    if event.key == pygame.K_b and self.game_over == False:
                        command = Command.B
                        self.factory = BombBlockTetrominoFactory()
                    if event.key == pygame.K_DOWN and self.game_over == False:
                        command = Command.DOWN
                        self.update_score(0, 1)
                    if event.key == pygame.K_UP and self.game_over == False:
                        command = Command.UP
                elif event.type == event_every_200ms and self.game_over == False:
                    command = Command.DOWN

            self.update(command)
            self.draw()
            pygame.display.update()

    def draw(self):
        """Draw the game elements on the screen."""
        self.ui.draw(self.screen, self)
        self.grid.draw(self.screen, 10, 10)
        self.tetromino.draw(self.screen, 10, 10)

    def update(self, command):
        """Update the game state based on the given command.

        Args:
            command (Command): The command to execute.
        """
        self.tetromino.update(command, self)

    def spawn_new_tetromino(self):
        """Spawn a new random tetromino."""
        return random.choice([TTetromino(), ITetromino(), OTetromino(),
                              ZTetromino(), STetromino(), JTetromino(),
                              LTetromino()])

    def check_for_any_full_lines_to_clear(self):
        """Check for any full lines in the grid and clear them."""
        return self.grid.check_for_any_full_lines_to_clear()

    def update_score(self, lined_cleared, move_down_points):
        """Update the game score based on the cleared lines and movements.

        Args:
            lined_cleared (int): Number of lines cleared.
            move_down_points (int): Points earned from moving down.
        """
        self.score += move_down_points
        if lined_cleared == 1:
            self.score += 100
        if lined_cleared == 2:
            self.score += 300
        if lined_cleared == 3:
            self.score += 500
