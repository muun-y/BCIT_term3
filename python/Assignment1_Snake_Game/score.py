import pygame


class Score:
    """
    Class to manage the score of the game.

    Attributes:
        font_size (int): The size of the font used for displaying the score. Default is 24.
        font_color (tuple): The color of the font used for displaying the score. Default is black (0, 0, 0).
        value (int): The current value of the score.
        font (pygame.font.Font): The font object used for rendering the score text.
        color (tuple): The color of the font used for rendering the score text.
    """

    def __init__(self, font_size=24, font_color=(0, 0, 0)):
        """
        Initialize the Score object.

        :args: font_size (int, optional): The size of the font used for displaying the score. Default is 24.
        :args: font_color (tuple, optional): The color of the font used for displaying the score. Default is black (0, 0, 0).
        """
        self.value = 0
        self.font = pygame.font.SysFont("Arial", font_size)
        self.color = font_color

    def increment_score(self):
        """Increment the score by 1."""
        self.value += 1

    def draw_score(self, screen):
        """
        Draw the current score on the screen.

        :args: screen (pygame.Surface): The surface on which to draw the score text.
        """
        score_text = self.font.render(f"Score: {self.value}", True, self.color)
        screen.blit(score_text, (10, 10))

    def get_score_text(self):
        """Get the text representation of the current score."""
        return f"{self.value}"

    def reset_score(self):
        """Reset the score to zero."""
        self.value = 0
