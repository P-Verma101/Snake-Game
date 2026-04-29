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
The 4 variables that are defined here are used to set up the
game window and game speed. Since this is a snake game, the

"""
GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 100
SPACE_SIZE = 50

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

