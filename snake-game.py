"""
The 2 import statements import python libraries that are used
in this code.
The 'import tkinter as tk' imports Python's bulit-in library
for the GUI library'tkinter'. This line imports the build-in
library as tk so the prefix 'tk.' is used to access the functions
and classes from the tkinter library. This imported library lets
you create windows, buttons, labels, etc.
The 'import random' imports the Python's build-in random library
that is typically used to generate random numbers.
"""
import tkinter as tk
import random

"""
The 4 variables that are defined here are constants. These are
values that are not to be changed and and are kind of like the
game's settings. 
The first variable that we have is 'GAME_WIDTH'which is set to 
700. This variable defines the width of the game window in pixels.

The second variable is the 'GAME_HEIGHT' which is also set to 
700. This variable defines the height of the game window in
pixels.

The third variable is 'SPEED' which is set to 100. This variable 
is used to control the speed of the snake in the game. The lower
the number, the faster the snake is. The higher the number, the
slower the snake is.

The fourth variable is 'SPACE_SIZE' which is set to 50. This
variable defines the size of each item in the game, such as the
food that the snake eats and the segments of the snake's body.

The fifth variable is 'BODY_PARTS' which is set to 3. This 
variable defines the number of 
"""
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3

class Snake:
    pass

class Food:
    pass

def next_turn():
    pass

def charge_direction(new_direction):
    pass

def check_collisions():
    pass

def game_over():
    pass

root = tk.Tk()
root.title("Snake Game")
root.mainloop()

