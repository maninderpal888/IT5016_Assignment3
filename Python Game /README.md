## Turtle Race Game
This is a simple Python program that simulates a race between two turtles using the Turtle graphics library.

## Requirements
-Python 3.10
-Turtle graphics library (usually included in Python standard library)

## How to Run
- Clone or download the repository to your local machine.
- Navigate to the directory containing the Python files.
- Run the turtle_race.py file using a Python interpreter.
- python game.py

## Gameplay
- Two turtles, one red and one blue, start at the same position on the screen.
- Each turtle moves forward by a fixed distance in a random direction (left or right) at each step.
- The race continues until one of the turtles reaches the edge of the screen or both turtles collide.
- The winner is determined based on which turtle remains on the screen or if both turtles collide.

## Files
- ***game.py: The main Python script containing the game logic.***
- ***README.md: This file, providing information about the game and how to run it.***

## Learning Concepts
This project incorporates several key programming concepts:

- Turtle Graphics: Utilize the turtle library to control virtual turtles on a canvas, creating engaging visualizations.
- Random Number Generation: Employ the random module to generate random values, introducing an element of chance into the turtle movements.
- Game Loop: Implement a while loop to continuously update the game state, ensuring a dynamic progression.
- Collision Detection: Design functions (isInScreen and samePosition) to identify collisions between turtles and screen boundaries.
- Event-Driven Programming: Although not explicitly implemented, this project lays the groundwork for understanding how user interactions (e.g., mouse clicks) could be used for further control (concept introduced).
