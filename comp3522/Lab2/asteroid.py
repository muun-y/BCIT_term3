class Asteroid:
    """Class representing an asteroid.

    Attributes:
        _id_counter (int): Counter to assign a unique ID to each asteroid instance.

    Methods:
        __init__(self, circumference, position, velocity):
            Initializes a new Asteroid instance.

        move(self):
            Moves the asteroid based on its velocity and returns the old position.

        __str__(self):
            Returns a string representation of the asteroid.

    """

    _id_counter = 0

    def __init__(self, circumference, position, velocity):
        """Initialize a new Asteroid instance.

        Args:
            circumference (float): The circumference of the asteroid.
            position (list): The initial position of the asteroid as a list [x, y, z].
            velocity (list): The initial velocity of the asteroid as a list [vx, vy, vz].

        """
        self._id = Asteroid._id_counter + 1
        Asteroid._id_counter += 1

        self._circumference = circumference
        self._position = Vector(*position)
        self._velocity = Vector(*velocity)

    def move(self):
        """Move the asteroid based on its velocity and return the old position."""
        old_position = self._position.as_tuple()
        self._position.add(self._velocity)
        return old_position

    def __str__(self):
        """Return a string representation of the asteroid."""
        return (
            f"Asteroid {self._id} is currently at {self._position}, "
            f"and moving at {self._velocity} metres per second. "
            f"It has a circumference of {self._circumference}"
        )


class Vector:
    """Class representing a 3D vector.

    Attributes:
        _x (float): The x-component of the vector.
        _y (float): The y-component of the vector.
        _z (float): The z-component of the vector.

    Methods:
        __init__(self, x, y, z):
            Initializes a new Vector instance.

        add(self, vector):
            Adds another vector to this vector.

        as_tuple(self):
            Returns the vector components as a tuple.

        __str__(self):
            Returns a string representation of the vector.

    """

    def __init__(self, x, y, z):
        """Initialize a new Vector instance.

        :param: x (float), the x-component of the vector.
        :param: y (float), the y-component of the vector.
        :param: z (float), the z-component of the vector.

        """
        self._x = x
        self._y = y
        self._z = z

    def add(self, vector):
        """Add another vector to this vector."""
        self._x += vector.x
        self._y += vector.y
        self._z += vector.z

    @property
    def x(self):
        """Getter for the x-component of the vector."""
        return self._x

    @property
    def y(self):
        """Getter for the y-component of the vector."""
        return self._y

    @property
    def z(self):
        """Getter for the z-component of the vector."""
        return self._z

    def as_tuple(self):
        """Return the vector components as a tuple."""
        return self._x, self._y, self._z

    def __str__(self):
        """Return a string representation of the vector."""
        return f"{self.x}, {self.y}, {self.z}"
