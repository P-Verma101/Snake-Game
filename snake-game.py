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
variable defines the number of body parts that the snake starts
with at the beginning of the game.

The sixth variable is 'SNAKE_COLOR' which is set to '#A0D9D3'.
This variable defines the color that the snake will have in
the game. The color is presented in hexidecimal format.

The seventh variable is 'FOOD_COLOR' which set to 'red'. This
variable defines the color of the food that the snake eats in
the game.

The eighth variable is 'BACKGROUND_COLOR' which is set to
'#00025B'. This variable defines the color of the background
in the game.
"""
GAME_WIDTH = 700 #--> Window width in pixels
GAME_HEIGHT = 700 #--> Window height in pixels
SPEED = 100 #--> Speed of the snake
SPACE_SIZE = 50 #--> Size of game items in pixels
BODY_PARTS = 3 #--> Number of body parts in beginning
SNAKE_COLOR = "#A0D9D3" #--> Color of snake body
FOOD_COLOR = "red" #--> Color of food that snake eats
BACKGROUND_COLOR = "#00025B" #--> Color of background in game


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

"""
This block of code is responsible for creating the main 
application window for the snake game. 
The first line of the code in this block creates the main
application window by calling 'tk.Tk()' and assigns it to the
variable 'root'. This creates an empty window that will serve as
the main window for the game.

The second line of the code block sets the title of the window
to "Snake Game" using the 'title' method of the 'root' window.

The third line of the code block uses the 'resizable' method of
the 'root' window to disable resizing of the window. The
arguments 'False, False' passed to the 'resizable' method
prevents the use from resizing the window in both the
horizontal and vertical directions.

The fourth line of the code block initalizes the score variable
to 0. This variable will be used to keep track of the player's
score in the game.

The fifth line of the code block initializes the direction of 
the snake to 'down'. This variable will be used to keep track 
of the current direction of the snake's movement in the game.

The sixth lin

The last line of the code block calls the 'mainloop' method of
the 'root' window. This method starts the main event loop of the
application, which keeps the window open and responsive to user
interactions. Without this line, the window would open and then
immediately close, as the program would finish executing.
"""
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

score = 0
direction = 'down'
label = tk.Label(root, text = "Score:{}".format(score), font = ("Arial", 40))
label.pack()

canvas = tk.Canvas(root, bg = BACKGROUND_COLOR, height = GAME_HEIGHT, width = GAME_WIDTH)
canvas.pack()

root.mainloop()

