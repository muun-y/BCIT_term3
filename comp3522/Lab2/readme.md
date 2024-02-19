[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=13421373&assignment_repo_type=AssignmentRepo)
# Off With a Bang

## Useful Links

- <https://docs.python.org/3.7/library/random.html#random.randint> . You will use the `randint` function available in the random module to generate random integers. Generating (pseudo-)random numbers in Python is trivially easy. Import the random module, and then access the function by using the module name and dot syntax. It accepts a lower bound (included) and an upper bound (included).
- <https://docs.python.org/3.7/library/datetime.html> . You will use the datetime module in this lab to ensure a program tracks movement over time.

## Asteroid Class

Implement a class called `Asteroid` in a file called `asteroid.py`:

- An Asteroid stores three attributes. `Circumference` in metres, `position`, `velocity`. Position and velocity are vectors composed of x, y, and z coordinates in 3D space measured in metres per second. Will you store them separately or as a list or as a tuple? Which choice creates the most maintainable code that is easiest to understand?

Optional:  

- See if you can create a `Vector` class that represents a vector in X, Y and Z dimensions and consists of the following:
  - Implements an `add(self, vector)` method which adds another vector to itself.
  - Implements properties that let you access the x, y and z values
  - A method that returns the vector as a tuple.
  - A `__str__(self)` method that would let you print a vector as a tuple.
- Create accessors and mutators as required. (or even properties!)
- Add a `move( )` method. The `move( )` method modifies the `position using` the velocity and returns the new position as a tuple of x, y and z coordinates. Recall that velocity is measured in metres per second. We have stored the velocity in three dimension. In order to implement `move( )`, we just need to add the amounts in the x, y, and z components of the velocity to the current position.
- Use statics to ensure each asteroid receives a sequential unique ID when it is created (start with 1). You will probably need to modify your initializer and create a helpful class method.
- Add a `__str__(self)` method to return the Asteroid's information in a single brief line of output.

## Controller Class

Implement a class called `Controller` in `driver.py`:

- `Controller` maintains a list of asteroid objects in the field.
- The `__init__(self, ...) `method must create some Asteroids and store them in the list. Each Asteroid should be assigned a random circumference, starting position and starting velocity.
  - Let's make 100 Asteroids with radius in the range [1, 4]. Calculate the circumference of the asteroid based on the radius.
  - Assuming that they are starting in a cube that is 100 metres per side
  - Each asteroid should have a velocity no greater than 5 metres per second in each direction.
  - Where should these methods go? In the controller? Or should some helper methods be added to the Asteroid (or Vector class if you have one)? Consider encapsulation and information hiding.
- Add a `simulate(self, seconds)` method. This method accepts a number of seconds. This method must ensure that every asteroid moves once per second for the number of specified seconds. You must use the datetime module to ensure that the looping begins precisely 'on the second'
  - If the current time is 5:05:05.7 there are 0.3 seconds until the next second begins. We must wait 0.3 seconds before we begin counting ‘on the second’
- Keep looping the simulation precisely on the second until the specified number of seconds have elapsed.

## Simulate

- Implement a main method where you instantiate a controller of Asteroids.
- Engage! (That's a Captain Picard reference)
- Ensure you push your work to github classroom.

I'd like to see sensible git commits comments, and commits must take place at logical points in development.

## Marking Scheme

- 80% Functionally
  - Created 100 asteroids  (-20% if not)
  - All asteroids have random positions (-20% if not)
  - Asteroids are properly adding vector amount to their position (-20% if not)
    - Asteroid 99 Moved! Old Pos: 47, 96, 92 -> New Pos: 52, 100, 96
    - Asteroid 99 is currently at 52, 100, 96 and moving at 5, 4, 4 metres per second. It has a circumference of 6.283185307179586
  - Actually starting the simulation on the exact time a new second begins (-10% if not)
- 20% documentation
![](https://cdn.discordapp.com/attachments/1149469347123830804/1153531168176754728/image.png)
