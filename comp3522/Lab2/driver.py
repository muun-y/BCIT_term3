from asteroid import Asteroid, Vector
from random import *
import datetime
import time


class Controller:
    """Controller class for simulating the movement of asteroids.

    Attributes:
        _asteroids (list): List of Asteroid instances representing the asteroids in the simulation.
        start_time (datetime.datetime): The start time of the simulation.

    Methods:
        __init__(self, num_asteroids):
            Initializes a new Controller instance with the specified number of asteroids

        _create_asteroids(self, num_asteroids):
            Creates and returns a list of Asteroid instances with random properties

        stimulate(self, seconds):
            Simulates the movement of asteroids for the specified number of seconds

    """

    def __init__(self, num_asteroids):
        """Initialize a new Controller instance


        :param:num_asteroids (int): The number of asteroids in the simulation

        """
        self._asteroids = self._create_asteroids(num_asteroids)
        self.start_time = None

    def _create_asteroids(self, num_asteroids):
        """Create and return a list of Asteroid instances with random properties

        :param: num_asteroids (int): The number of asteroids to create
        :return: the list of Asteroid instances

        """
        asteroids = []
        for _ in range(1, num_asteroids + 1):
            radius = randint(1, 4)
            circumference = 2 * 3.141592653589793 * radius
            position = [randint(0, 100) for _ in range(3)]
            velocity = [randint(-4, 4) for _ in range(3)]

            asteroid = Asteroid(circumference, position, velocity)
            asteroids.append(asteroid)
        return asteroids

    def stimulate(self, seconds):
        """Simulate the movement of asteroids for the specified number of seconds.

        :param seconds (int): The number of seconds to simulate.

        """
        start_time = datetime.datetime.now()
        print(f"Simulation Start Time: {start_time}")
        print("\nMoving Asteroids!")
        print("\n-----------------")
        current_time = start_time

        while (current_time - start_time).total_seconds() < seconds:
            time.sleep(1 - current_time.microsecond / 1e6)
            current_time = datetime.datetime.now()
            for asteroid in self._asteroids:
                old_position = asteroid.move()
                print(
                    f"Asteroid {asteroid._id} Moved! Old Pos: {old_position[0]}, {old_position[1]}, {old_position[2]} -> New Pos: {asteroid._position.x}, {asteroid._position.y}, {asteroid._position.z}"
                )
                print(str(asteroid))


if __name__ == "__main__":
    controller = Controller(100)
    controller.stimulate(10)
