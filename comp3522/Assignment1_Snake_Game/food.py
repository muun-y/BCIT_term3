import pygame
import random


class Food:
    """
    Class representing food in the game.

    Attributes:
        x (int): The x-coordinate of the food.
        y (int): The y-coordinate of the food.
        screen (pygame.Surface): The screen where the food will be drawn.
    """

    def __init__(self, x, y, screen):
        """
        Initialize the Food object.

        :args: x (int): The x-coordinate of the food.
        :args: y (int): The y-coordinate of the food.
        :args: screen (pygame.Surface): The screen where the food will be drawn.
        """
        self.x = x
        self.y = y
        self.screen = screen

    def draw_food(self):
        """
        Draw the food on the screen as a rectangle.
        """
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, 40, 40))

    def get_position(self):
        """
        Get the position of the food.

        Returns:
            dict: A dictionary containing the x and y coordinates of the food.
        """
        return {"x": self.x, "y": self.y}

    def randomize_food_position(self, snake_segments):
        """
        Randomly set the position of the food, ensuring it is not on the snake.

        :args: snake_segments (list): A list containing the segments of the snake.
        """
        while True:
            x = random.randint(0, 19) * 40  # Random x position
            y = random.randint(0, 19) * 40  # Random y position
            # Check if the new position is not on the snake
            if (x, y) not in [(seg["x"], seg["y"]) for seg in snake_segments]:
                self.x = x
                self.y = y
                break
