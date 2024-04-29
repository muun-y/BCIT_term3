"""
This module implements the Tetromino classes and factories for a Tetris game.
- Asbtract base class Tetromino defines the common attributes and methods for all Tetrominos.
- Concrete Tetromino classes implement the Tetromino shapes and behavior.
- TetrominoFactory abstract base class defines the interface for creating Tetrominos.
- Concrete TetrominoFactory classes implement the Tetromino creation logic.
- Tetrominos can be moved, rotated, and frozen in the game
"""

import pygame
from command import Command
from resources.colors import Colors
import abc
import time


class Tetromino:
    """
    Abstract base class representing a Tetromino.

    Attributes:
    - state: Current state of the Tetromino.
    - col_offset: Column offset for positioning the Tetromino.
    - row_offset: Row offset for positioning the Tetromino.
    - frozen: Flag indicating if the Tetromino is frozen.
    - freeze_timer: Timer for freezing the Tetromino.
    """
    def __init__(self) -> None:
        """Initialize common attributes of a Tetromino."""
        self.state = 0
        self.col_offset = 4
        self.row_offset = 0
        self.frozen = False
        self.freeze_timer = None

    def draw(self, screen, ui_x_offset, ui_y_offset):
        """
        Draw the Tetromino on the screen.

        Args:
        - screen: Pygame screen object to draw on.
        - ui_x_offset: X offset for the UI.
        - ui_y_offset: Y offset for the UI.
        """
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (
                            (col_index + self.col_offset) * 30 + ui_x_offset,
                            (row_index + self.row_offset) * 30 + ui_y_offset,
                            30 - 1,
                            30 - 1,
                        ),
                    )

                    if self.frozen == True:
                        pygame.draw.rect(
                            screen,
                            (255, 0, 0),
                            (
                                (col_index + self.col_offset) * 30 + ui_x_offset,
                                (row_index + self.row_offset) * 30 + ui_y_offset,
                                30,
                                30,
                            ),
                            10,  # Thickness of the border
                        )
                        font = pygame.font.Font(None, 36)
                        text = font.render("Freeze", True, Colors.WHITE.value)
                        text_rect = text.get_rect(center=(
                            (col_index + self.col_offset) * 30 + ui_x_offset + 15,
                            (row_index + self.row_offset) * 30 + ui_y_offset + 15
                        ))
                        screen.blit(text, text_rect)

    def update(self, command: Command, game):
            """
        Update the Tetromino based on the given command.

        Args:
        - command: Command enum specifying the action to perform.
        - game: Game object containing game state and logic.
        """
            if command == Command.LEFT:
                self.move_left(game)
            if command == Command.RIGHT:
                self.move_right(game)
            if command == Command.DOWN:
                self.move_down(game)
            if command == Command.UP:
                self.rotate()
            if command == Command.F:  
                self.freeze(game)
        

    def move_left(self, game):
        """Move the Tetromino left."""
        self.col_offset -= 1
        if self.out_of_bounds():
            self.col_offset += 1

        if self.collides_with_other_tetrominos(game):
            self.col_offset += 1

    def move_right(self, game):
        """Move the Tetromino right."""
        self.col_offset += 1
        if self.out_of_bounds():
            self.col_offset -= 1

        if self.collides_with_other_tetrominos(game):
            self.col_offset -= 1

    def move_down(self, game):
        """Move the Tetromino down."""
        self.row_offset += 1

        if self.collides_with_other_tetrominos(game):
            self.row_offset -= 1
            if self.row_offset <= 0:
                print("game over")
                game.game_over = True
                return
            self.lock_tetromino(game)
            game.tetromino = game.next_tetromino
            game.next_tetromino = game.spawn_new_tetromino()
            return

        if self.out_of_bounds():
            self.row_offset -= 1
            self.lock_tetromino(game)
            game.tetromino = game.next_tetromino
            game.next_tetromino = game.spawn_new_tetromino()
            return

    def out_of_bounds(self):
        """Check if the Tetromino is out of bounds."""
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    if (
                        col_index + self.col_offset < 0
                        or col_index + self.col_offset > 9
                        or row_index + self.row_offset > 19
                    ):
                        return True
        return False

    def rotate(self):
        """Rotate the Tetromino."""
        self.state = (self.state + 1) % len(self.blocks)
        if self.out_of_bounds():
            self.state = (self.state - 1) % len(self.blocks)

    def lock_tetromino(self, game):
        """
        Carbon copy the tetromino into the grid
        """
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    game.grid.blocks[row_index + self.row_offset][
                        col_index + self.col_offset
                    ] = self.color
        lined_cleared = game.check_for_any_full_lines_to_clear()
        game.update_score(lined_cleared, 0)

    def collides_with_other_tetrominos(self, game):
        """
        Check if the Tetromino collides with other Tetrominos on the grid.

        Args:
        - game: Game object containing game state and logic.

        Returns:
        - True if collision detected, False otherwise.
        """
        for row_index, row in enumerate(self.blocks[self.state]):
            for col_index, block in enumerate(row):
                if block:
                    if row_index + self.row_offset <= 19:
                        if game.grid.blocks[row_index + self.row_offset][
                            col_index + self.col_offset
                        ]:
                            return True
        return False
    
    def freeze(self, game):
        """
        Freeze the Tetromino temporarily.

        Args:
        - game: Game object containing game state and logic.
        """
        self.frozen = True  
        start_time = time.time()  
        while time.time() - start_time < self.freeze_duration:
            keys = pygame.key.get_pressed()  
            if keys[pygame.K_DOWN]:
                self.move_down(game)
            if keys[pygame.K_LEFT]:
                self.move_left(game)
            if keys[pygame.K_RIGHT]:
                self.move_right(game)
            pygame.time.wait(10)  
        
    
        self.frozen = False


class ZTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.BLUE.value
        self.freeze_duration = 1.5  
        self.blocks = [
            [
                [1, 1, 0],
                [0, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 0, 1],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [1, 0, 0],
            ],
        ]


class BasicZTetromino(ZTetromino):
    def __init__(self) -> None:
        super().__init__()


class FreezeZTetromino(ZTetromino):
    def __init__(self) -> None:
        super().__init__()

class BombZTetromino(ZTetromino):
    def __init__(self) -> None:
        super().__init__()
        self.border_color = Colors.RED.value


class OTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.YELLOW.value
        self.freeze_duration = 5.0 
        self.blocks = [
            [
                [1, 1],
                [1, 1],
            ]
        ]


class BasicOTetromino(OTetromino):
    def __init__(self) -> None:
        super().__init__()


class FreezeOTetromino(OTetromino):
    def __init__(self) -> None:
        super().__init__()
    


class BombOTetromino(OTetromino):
    def __init__(self) -> None:
        super().__init__()
        self.border_color = Colors.RED.value


class ITetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.ORANGE.value
        self.freeze_duration = 7.0 
        self.blocks = [
            [
                [0, 0, 0, 0],
                [1, 1, 1, 1],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
            ],
            [
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
                [0, 0, 1, 0],
            ],
        ]
        self.col_offset = 3
        self.row_offset = -1


class BasicITetromino(ITetromino):
    def __init__(self) -> None:
        super().__init__()


class FreezeITetromino(ITetromino):
    def __init__(self) -> None:
        super().__init__()


class BombITetromino(ITetromino):
    def __init__(self) -> None:
        super().__init__()
        self.border_color = Colors.RED.value


class STetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.PURPLE.value
        self.freeze_duration = 4.0 
        self.blocks = [
            [
                [0, 1, 1],
                [1, 1, 0],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 0, 1],
            ],
            [
                [0, 0, 0],
                [0, 1, 1],
                [1, 1, 0],
            ],
            [
                [1, 0, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ]


class BasicSTetromino(STetromino):
    def __init__(self) -> None:
        super().__init__()


class FreezeSTetromino(STetromino):
    def __init__(self) -> None:
        super().__init__()

class BombSTetromino(STetromino):
    def __init__(self) -> None:
        super().__init__()
        self.border_color = Colors.RED.value


class JTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.RED.value
        self.freeze_duration = 5.5 
        self.blocks = [
            [
                [1, 0, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 1],
                [0, 1, 0],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 0, 1],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [1, 1, 0],
            ],
        ]


class BasicJTetromino(JTetromino):
    def __init__(self) -> None:
        super().__init__()


class FreezeJTetromino(JTetromino):
    def __init__(self) -> None:
        super().__init__()


class BombJTetromino(JTetromino):
    def __init__(self) -> None:
        super().__init__()
        self.border_color = Colors.RED.value


class LTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.GREEN.value
        self.freeze_duration = 3.5 
        self.blocks = [
            [
                [0, 0, 1],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 0],
                [0, 1, 1],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [1, 0, 0],
            ],
            [
                [1, 1, 0],
                [0, 1, 0],
                [0, 1, 0],
            ],
        ]


class BasicLTetromino(LTetromino):
    def __init__(self) -> None:
        super().__init__()


class FreezeJLTetromino(LTetromino):
    def __init__(self) -> None:
        super().__init__()

class BombLTetromino(LTetromino):
    def __init__(self) -> None:
        super().__init__()
        self.border_color = Colors.RED.value


class TTetromino(Tetromino):
    def __init__(self) -> None:
        super().__init__()
        self.color = Colors.CYAN.value
        self.freeze_duration = 2.5
        self.blocks = [
            [
                [0, 1, 0],
                [1, 1, 1],
                [0, 0, 0],
            ],
            [
                [0, 1, 0],
                [0, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 0, 0],
                [1, 1, 1],
                [0, 1, 0],
            ],
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 1, 0],
            ],
        ]


class BasicTTetromino(TTetromino):
    def __init__(self) -> None:
        super().__init__()


class FreezeTTetromino(TTetromino):
    def __init__(self) -> None:
        super().__init__()
        


class BombTTetromino(TTetromino):
    def __init__(self) -> None:
        super().__init__()
        self.border_color = Colors.RED.value


class TetrominoFactory(abc.ABC):
    """Abstract base class for Tetromino factories."""
    @abc.abstractmethod
    def create_z_tetromino(self) -> ZTetromino:
        """Create a Z Tetromino."""
        pass

    @abc.abstractmethod
    def create_o_tetromino(self) -> OTetromino:
        """Create a O Tetromino."""
        pass

    @abc.abstractmethod
    def create_i_tetromino(self) -> ITetromino:
        """Create a I Tetromino."""
        pass

    @abc.abstractmethod
    def create_s_tetromino(self) -> STetromino:
        """Create a S Tetromino."""
        pass

    @abc.abstractmethod
    def create_j_tetromino(self) -> JTetromino:
        """Create a J Tetromino."""
        pass

    @abc.abstractmethod
    def create_l_tetromino(self) -> LTetromino:
        """Create a L Tetromino."""
        pass

    @abc.abstractmethod
    def create_t_tetromino(self) -> TTetromino:
        """Create a T Tetromino."""
        pass


class BasicTetrominoFactory(TetrominoFactory):
    """Factory for creating basic Tetrominos."""
    def create_z_tetromino(self) -> ZTetromino:
        return BasicZTetromino()

    def create_o_tetromino(self) -> OTetromino:
        return BasicOTetromino()

    def create_i_tetromino(self) -> ITetromino:
        return BasicITetromino()

    def create_s_tetromino(self) -> STetromino:
        return BasicSTetromino()

    def create_j_tetromino(self) -> JTetromino:
        return BasicJTetromino()

    def create_l_tetromino(self) -> LTetromino:
        return BasicLTetromino()

    def create_t_tetromino(self) -> TTetromino:
        return BasicTTetromino()


class FreezePowerupTetrominoFactory(TetrominoFactory):
    """Factory for creating freeze Tetrominos."""
    def create_z_tetromino(self) -> ZTetromino:
        return FreezeZTetromino()

    def create_o_tetromino(self) -> OTetromino:
        return FreezeOTetromino()

    def create_i_tetromino(self) -> ITetromino:
        return FreezeITetromino()

    def create_s_tetromino(self) -> STetromino:
        return FreezeSTetromino()

    def create_j_tetromino(self) -> JTetromino:
        return FreezeJTetromino()

    def create_l_tetromino(self) -> LTetromino:
        return FreezeJTetromino()

    def create_t_tetromino(self) -> TTetromino:
        return FreezeTTetromino()


class BombBlockTetrominoFactory(TetrominoFactory):
    """Factory for creating Bombblock Tetrominos."""
    def create_z_tetromino(self) -> ZTetromino:
        return BombZTetromino()

    def create_o_tetromino(self) -> OTetromino:
        return BombOTetromino()

    def create_i_tetromino(self) -> ITetromino:
        return BombITetromino()

    def create_s_tetromino(self) -> STetromino:
        return BombSTetromino()

    def create_j_tetromino(self) -> JTetromino:
        return BombJTetromino()

    def create_l_tetromino(self) -> LTetromino:
        return BombLTetromino()

    def create_t_tetromino(self) -> TTetromino:
        return BombTTetromino()