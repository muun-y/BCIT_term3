from direction import Direction

"""CollisionDetector Class

This class detects collisions between the snake and various game elements,
such as food, walls, and itself.

Attributes:
    segments (list): List of segments comprising the snake's body.
    block_size (int): Size of each block in pixels.

"""


class CollisionDetector:
    """Detects collisions between the snake and game elements."""

    def __init__(self, segments, block_size):
        """Initialize the collision detector.

        :args: segments (list): List of segments comprising the snake's body.
        :args: block_size (int): Size of each block in pixels.

        """
        self.segments = segments
        self.block_size = block_size

    def detect_collision_with_food(self, food):
        """Detect collision between the snake and food.


        :args:food (Food): The food object representing the position of the food.

        :returs: bool: True if collision with food, False otherwise.

        """
        if (self.segments[-1]["x"] == food.x) and (self.segments[-1]["y"] == food.y):
            return True

    def detect_collision_with_wall(self):
        if self.segments[-1]["x"] < 0 or self.segments[-1]["x"] > 760:
            return True
        elif self.segments[-1]["y"] < 0 or self.segments[-1]["y"] > 760:
            return True

    def detect_collision_with_itself(self):
        """Detect collision between the snake and walls.

        :returns bool: True if collision with walls, False otherwise.

        """
        if self.segments[-1] in self.segments[:-1]:
            return True


"""AutoPilotMode Class

This class implements the autopilot mode for the snake. It calculates the
optimal path to reach the food using the A* algorithm and updates the snake's
direction accordingly.

Attributes:
    snake (Snake): The snake object controlled by the autopilot.

"""


class AutoPilotMode:
    """Represents the autopilot mode for the snake."""

    def __init__(self, snake):
        """Initialize the autopilot mode.

        :args: snake (Snake): The snake object controlled by the autopilot.

        """
        self.snake = snake

    def find_neighbors(self, a_segment):
        """Find neighboring segments of a given segment.

        :args: a_segment (dict): The segment for which neighbors are to be found.

        :returns list: List of neighboring segments.

        """
        neighbors = []
        if a_segment["x"] < 760:
            neighbors.append(
                {"x": a_segment["x"] + self.snake.block_size, "y": a_segment["y"]}
            )
        if a_segment["x"] > 0:
            neighbors.append(
                {"x": a_segment["x"] - self.snake.block_size, "y": a_segment["y"]}
            )
        if a_segment["y"] < 760:
            neighbors.append(
                {"x": a_segment["x"], "y": a_segment["y"] + self.snake.block_size}
            )
        if a_segment["y"] > 0:
            neighbors.append(
                {"x": a_segment["x"], "y": a_segment["y"] - self.snake.block_size}
            )
        return neighbors

    def find_valid_neighbors(self, neighbors):
        """Find valid neighboring segments that are not part of the snake.

        :args: neighbors (list): List of neighboring segments.

        :returns: list: List of valid neighboring segments.

        """
        valid_neighbors = []
        for neighbor in neighbors:
            if neighbor not in self.snake.segments:
                valid_neighbors.append(neighbor)
        return valid_neighbors

    def find_path(self, food):
        """Find the optimal path to reach the food using the A* algorithm.

        :args: food (Food): The food object representing the position of the food.

        :returns list: List of segments representing the optimal path.

        """
        visited = []  # set
        queue = []  # queue

        path_to_the_head = [self.snake.segments[-1]]
        queue.append((self.snake.segments[-1], path_to_the_head))

        while queue:
            a_segment, path = queue.pop(0)
            if a_segment == food.get_position():
                self.snake.final_path = path
                self.snake.visited = visited
                return path

            neighbors = self.find_neighbors(a_segment)
            valid_neighbors = self.find_valid_neighbors(neighbors)

            for neighbor in valid_neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append((neighbor, path + [neighbor]))
        return None

    def update_direction(self, food):
        """Update the direction of the snake based on the calculated path.

        :args food (Food): The food object representing the position of the food.

        """
        path = self.find_path(food)
        if path:
            next_segment = path[1]
            if next_segment["x"] > self.snake.segments[-1]["x"]:
                self.snake.direction = Direction.RIGHT
            elif next_segment["x"] < self.snake.segments[-1]["x"]:
                self.snake.direction = Direction.LEFT
            elif next_segment["y"] > self.snake.segments[-1]["y"]:
                self.snake.direction = Direction.DOWN
            elif next_segment["y"] < self.snake.segments[-1]["y"]:
                self.snake.direction = Direction.UP
