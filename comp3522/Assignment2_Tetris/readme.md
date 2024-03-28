
# Assignment 2: Abstract Factory Design Pattern with Tetris Game

## Part 1  - Build a Tetris Game

**Objective:**  By completing this part, you will learn and a functional Tetris game using the Pygame library.

**Demo and a Tutorial:**

- <https://youtu.be/WdX9XXkSkOA>

**Tasks:**

1. **Install Pygame** (If not already done)
2. **Setup the Game Loop:**
    - Create a basic Pygame window.
    - Implement a game loop that handles events, updates game logic, and renders graphics.

3. **Creating the Grid:**
    - Design a data structure to represent the Tetris grid (e.g., a 2D array).
    - Visually draw the grid on the Pygame window.

4. **Create Tetrominoes:**
    - Define different Tetromino shapes (I, O, T, J, L, S, Z) using their block configurations.
    - Implement a way to randomly select a Tetromino at the start of each turn.

5. **Move Tetrominoes:**
    - Allow user input to control Tetromino movement:
        - Left and right
        - Down (soft drop)
    - Ensure Tetrominoes stay within grid boundaries.

6. **Rotate Tetrominoes:**
    - Allow user input to rotate Tetrominoes.
    - Prevent rotations that would place Tetrominoes outside the grid.

7. **Checking for Collisions:**
    - Implement gravity: Tetrominoes fall automatically over time.
    - When a Tetromino reaches the bottom or collides with another Tetromino:
        - "Lock" the Tetromino in place.

8. **Check for Completed Rows:**
    - After each Tetromino locks, scan for full horizontal rows.
    - Clear completed rows, and shift all rows above them down.

9. **Game Over:**
    - Detect when a new Tetromino cannot be placed at its starting position.
    - End the game and display a "Game Over" message.

10. **Create User Interface:**
    - Display a "Next Block" preview area.
    - Display the current score.

11. **Add Score:**
    - Award points for clearing lines:
        - 1 line: 100 points
        - 2 lines: 300 points
        - 3 lines: 500 points
    - Award a small number of points for each Tetromino's downward movement (soft drop).

12. **Add Next Block**
    - Display a preview of the upcoming Tetromino shape.

## Part II: Power-ups and Design Patterns

**Objective:**  Enhance your Tetris game by adding power-up Tetrominoes and using the abstract factory design pattern to manage their creation. This will solidify your understanding of object-oriented programming and design patterns.

**Demo:**

- <https://youtu.be/zqIBbYXNaV0>

**Tasks:**

1. Add **FreezePowerupTetromino:** type of Tetromino that slows down the game's speed temporarily. The Freezed Tetromino induces a temporary state where the normal flow of the game slows down or pauses for a predefined duration.  Effect Duration is customizable.
    - Design a `FreezePowerupTetromino` class.
    - Implement the effect of this Tetromino:
        - When activated, temporarily slow down the game's speed (i.e., the falling speed of all Tetrominoes) for a set duration.  
        - Each Tetromino can have a customizable freeze duration.
    - For testing, this power-up should also be activated by the player (e.g., by pressing a specific key).

2. Add **BombBlockTetromino:** type of Tetromino that triggers an explosion when it locks into place. This effect can clear surrounding blocks or lines, creating space for the player to continue building and preventing the game board from becoming too crowded. Range and Pattern are customizable for the explosion.
    - Design a `BombBlockTetromino` class.
        - Each Tetromino shape has a unique explosion pattern and range.
        - Each Tetromino shape has a unique darkened color to indicate it's a bomb.
    - Implement the effect of this Tetromino:
        - When it locks into place, trigger an explosion that clears surrounding blocks or lines within a customizable radius.
    - For testing, this power-up should also be activated by the player (e.g., by pressing a specific key).

3. Add the needed factory classes using the *Abstract Factory* design pattern.

**Integration:**

- Update your game logic to randomly include power-up Tetrominoes from the `PowerupTetrominoFactory` with a set probability.
- Allow players to activate the power-up effects (e.g., by pressing a specific key).

**Considerations:**

- **Balance:** Ensure the power-ups are fun additions without making the game too easy.
- **Visuals:** Consider adding visual effects to indicate the Freeze and Bomb power-ups, enhancing the gameplay experience.

- Update your code with the abstract factory implementation and power-up Tetrominoes.
- In the YT video, Briefly explain your design choices for the abstract factory pattern and the power-up behaviors.

## Submission/Deliverables

- Submit your a Github classroom link for your Python code.
- Submit a 2-3 minutes max for a Youtube link to a video of your game in action. State any design decisions you made and why you made them.

## Marking Scheme

| Criteria | Points | Description |
|---|---|---|
**Part 1: Build a Tetris Game (70 points)**|  |   |
| Core Game Mechanics | 40 | Grid representation (5); Tetromino shapes & generation (5); Movement with boundary checks (10); Rotation (10); Collision detection & locking (10) |
| Line Clearing & Game Over| 15 |  Detecting full rows (5); Clearing rows & shifting blocks (5), Game over logic (5) |
| User Interface & Scoring| 15 | Next block preview (5); Score display (5); Scoring system (5)|
**Part 2: Power-ups and Design Patterns (30 points)** | |  |
| Abstract Factory Implementation | 15 | Abstract Factory class(es) (3); Concrete factories (6); Correct pattern usage (6) |
| Power-up Tetrominoes | 15 | `FreezePowerupTetromino`s (7); `BombBlockTetromino`s (7); Integration (1) |
**Additional Considerations** | |  |
| Code Quality | 5 | Readability, comments, naming conventions |
| Gameplay and Balance | 5 | Fun factor, difficulty, power-up effectiveness |
**Submission/Deliverables** | |  |
| GitHub Classroom Link | Mandatory |  |
| YouTube Video | Mandatory | Explanation of design choices and gameplay demonstration |

## Tips for Development Strategy

- **Work incrementally** – test each part as you build it.
- Refer to Pygame documentation and online tutorials for examples.
- Start with the core mechanics, then add the UI and scoring later.

- **Start Simple, Then Expand:** Begin by implementing the standard Tetromino types and game mechanics. Once that's solid, introduce the abstract factory design pattern and then the power-ups.

- **Design Before Coding:**  Think carefully about the classes you'll need and their relationships *before* you start writing code. Sketch out class diagrams to help you visualize the abstract factory structure.

- **Modularize:** Break down your code into well-defined functions and classes as this will aid in adding the power-ups more smoothly.

- **Test, Test, Test:** Test each feature thoroughly as you add it. Debug and fix problems early!

- **Balance the Power-ups:** Experiment with different effect durations and explosion ranges and patterns to make sure the power-ups are challenging and fun without being overpowered.

- **Visual Feedback Is Key:** Design clear visual indicators for when power-ups are active (e.g., slowing down the game with a visual effect for Freeze, and a flashy explosion for the Bomb).
