import pygame
from snake import Snake
from food import Food
from score import Score
from direction import Direction


class Game:
    """Represents the main game logic and loop.

    Attributes:
        game_board (GameBoard): The game board for the game.
    """

    def __init__(self, game_board):
        """Initialize the game with a game board."""
        self.game_board = game_board

    def run_game(self):
        """Run the game loop."""
        clock = pygame.time.Clock()
        FPS = 15
        pause = False

        # Game loop
        running = True
        while running:
            # Check for the events
            clock.tick(FPS)  # 1 frame per second
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if not pause:
                        if event.key == pygame.K_UP:
                            self.game_board.snake.direction = Direction.UP
                        elif event.key == pygame.K_DOWN:
                            self.game_board.snake.direction = Direction.DOWN
                        elif event.key == pygame.K_LEFT:
                            self.game_board.snake.direction = Direction.LEFT
                        elif event.key == pygame.K_RIGHT:
                            self.game_board.snake.direction = Direction.RIGHT
                        elif event.key == pygame.K_a:
                            self.game_board.snake.auto_pilot = True
                    else:
                        if event.key == pygame.K_SPACE:
                            pause = False
                            self.game_board.snake = Snake(
                                40, 40, self.game_board.screen, self.game_board.score
                            )

            try:
                if not pause:
                    self.update_game()
                    self.draw_game()
            except Exception as e:
                print(e)
                pause = True
                self.game_over()  # to display the text "Game Over"

    def update_game(self):
        """Update the game state."""
        if self.game_board.snake.update_snake(
            self.game_board.food
        ):  # Returns True if food eaten
            self.game_board.score.increment_score()  # Increment score when food eaten
            self.game_board.food.randomize_food_position()  # Move food to a new position

    def draw_game(self):
        """Draw the game objects on the screen."""
        self.game_board.screen.fill((255, 255, 255))
        self.game_board.score.draw_score(self.game_board.screen)
        self.game_board.snake.draw_snake()
        self.game_board.food.draw_food()

        # update the display
        pygame.display.flip()

    def game_over(self):
        """Display the game over message and reset the score."""
        # fill
        self.game_board.screen.fill((255, 255, 255))
        font = pygame.font.SysFont("Arial", 30)
        score_text = self.game_board.score.get_score_text()
        text = font.render(
            f"Game Over. Your score is {score_text}. Hit Space to restart! ",
            True,
            (0, 0, 0),
        )
        self.game_board.screen.blit(
            text, (400 - text.get_width() / 2, 400 - text.get_height() / 2)
        )
        pygame.display.flip()

        # reset the score after the score is displayed
        self.game_board.score.reset_score()


class GameBoard:
    """Represents the game board.

    Attributes:
        screen (pygame.Surface): The surface of the game window.
        score (Score): The score of the game.
        snake (Snake): The snake object in the game.
        food (Food): The food object in the game.
    """

    def __init__(self, width, height):
        """Initialize the game board with given width and height."""
        pygame.init()
        # Create a window
        self.screen = pygame.display.set_mode((width, height))

        # Set the title of the window
        pygame.display.set_caption("Snake Game")

        # Fill the background color of the window
        self.screen.fill((255, 255, 255))  # white color

        # create score object
        self.score = Score()

        # game objects
        self.snake = Snake(40, 40, self.screen, self.score)
        self.food = Food(200, 200, self.screen)
