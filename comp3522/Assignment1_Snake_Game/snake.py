"""Snake Class

This class represents the snake in the game. It handles the snake's movement,
collision detection, and drawing on the screen.

Attributes:
    screen (pygame.Surface): The surface of the game window.
    score (Score): The score object tracking the player's score.
    direction (Direction): The current direction of the snake.
    block_size (int): The size of each segment of the snake.
    segments (list): List of dictionaries representing the segments of the snake.
    auto_pilot (bool): Flag indicating whether the snake is in autopilot mode.
    final_path (list): List of segments representing the final path determined by autopilot.
    visited (list): List of segments representing the visited segments by the autopilot.
    collision_detector (CollisionDetector): Object for detecting collisions.

"""

import pygame
from direction import Direction
from snakefunction import AutoPilotMode, CollisionDetector


class Snake:
    """Represents the snake in the game."""

    def __init__(self, x, y, screen, score):
        """Initialize the snake.

        :args: x (int): The x-coordinate of the snake's starting position.
        :args: y (int): The y-coordinate of the snake's starting position.
        :args: screen (pygame.Surface): The surface of the game window.
        :args: score (Score): The score object tracking the player's score.

        """
        self.screen = screen
        self.score = score
        self.direction = Direction.RIGHT
        self.block_size = 40
        self.segments = [
            {"x": x, "y": y},
            {"x": x + self.block_size, "y": y},
            {"x": x + self.block_size * 2, "y": y},
            {"x": x + self.block_size * 3, "y": y},
        ]
        self.auto_pilot = False
        self.final_path = []
        self.visited = []
        self.collision_detector = CollisionDetector(self.segments, self.block_size)

    def draw_visited_segments(self):
        """Draw visited segments of the snake."""
        for segment in self.visited:
            pygame.draw.rect(
                self.screen,
                (66, 135, 245),  # blue
                (segment["x"], segment["y"], self.block_size, self.block_size),
            )

    def draw_final_path(self):
        """Draw the final path determined by autopilot."""
        for segment in self.final_path:
            pygame.draw.rect(
                self.screen,
                (252, 186, 3),  # yellow
                (segment["x"], segment["y"], self.block_size, self.block_size),
                2,
            )

    def draw_snake_segments(self):
        """Draw the segments of the snake."""
        for segment in self.segments:
            pygame.draw.rect(
                self.screen,
                (0, 0, 0),
                (segment["x"], segment["y"], self.block_size, self.block_size),
            )

    def draw_snake(self):
        """Draw the snake on the screen."""
        self.draw_visited_segments()
        self.draw_final_path()
        self.draw_snake_segments()

    def update_snake(self, food):
        """Update the position of the snake.

        :args: food (Food): The food object for collision detection.

        Raises:
            Exception: If the snake collides with the wall or itself.

        """

        # update the body of the snake
        for i in range(len(self.segments) - 1):
            self.segments[i]["x"] = self.segments[i + 1]["x"]
            self.segments[i]["y"] = self.segments[i + 1]["y"]

        if self.auto_pilot == True:
            auto_pilot = AutoPilotMode(self)
            auto_pilot.update_direction(food)

        # update the head of the snake
        if self.direction == Direction.RIGHT:
            self.segments[-1]["x"] += self.block_size
        elif self.direction == Direction.LEFT:
            self.segments[-1]["x"] -= self.block_size
        elif self.direction == Direction.UP:
            self.segments[-1]["y"] -= self.block_size
        elif self.direction == Direction.DOWN:
            self.segments[-1]["y"] += self.block_size

        # detect collision with food,
        if self.collision_detector.detect_collision_with_food(food):
            self.increase_the_size_of_snake_by_one()
            self.score.increment_score()
            food.randomize_food_position(
                [segment.copy() for segment in self.segments]
            )  # Move food to a new position

        # detect collision with the wall
        if self.collision_detector.detect_collision_with_wall():
            raise Exception("Game over - collision with the wall")

        # detect collision with itself
        if self.collision_detector.detect_collision_with_itself():
            raise Exception("Game over - collision with itself")

    def increase_the_size_of_snake_by_one(self):
        """Increase the size of the snake by one segment."""
        if self.direction == Direction.RIGHT:
            self.segments.append(
                {
                    "x": self.segments[-1]["x"] + self.block_size,
                    "y": self.segments[-1]["y"],
                }
            )
        elif self.direction == Direction.LEFT:
            self.segments.append(
                {
                    "x": self.segments[-1]["x"] - self.block_size,
                    "y": self.segments[-1]["y"],
                }
            )
        elif self.direction == Direction.UP:
            self.segments.append(
                {
                    "x": self.segments[-1]["x"],
                    "y": self.segments[-1]["y"] - self.block_size,
                }
            )
        elif self.direction == Direction.DOWN:
            self.segments.append(
                {
                    "x": self.segments[-1]["x"],
                    "y": self.segments[-1]["y"] + self.block_size,
                }
            )
