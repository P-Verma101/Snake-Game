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
SNAKE_COLOR = "#46E28C" #--> Color of snake body
FOOD_COLOR = "red" #--> Color of food that snake eats
BACKGROUND_COLOR = "#00025B" #--> Color of background in game

"""
This block of code defines the 'Snake' class and its
'__init__' constructor, whic creates a 3-segment snake at
position (0, 0) on the canvas.
 
The first line of code defines the 'Snake' class.

The Second line of code is the constructor method. It runs
automatically when the 'snake = Snake()' is done. The 
'__init__' is the initializer, 'self' is the reference to
this snake instance. It sets up nwe snake when created.

The third line of code is 'self.body_size = BODY_PARTS'.
The purpose of this line is to sture the inital snake 
length. Since we established that the body length of the 
snake is 3 with the 'BODY_PARTS = 3' constant this line
is essentially an instance variable. It is unique to this
snake.

The fourth line is 'self.coordinates = []'
"""
class Snake:

    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range (0, BODY_PARTS):
            self.coordinates.append ([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = SNAKE_COLOR, tag = "Snake")

class Food:

    def __init__(self):
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE) - 1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill = FOOD_COLOR, tag = "Food")

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

The sixth line of this code block creates a label variable
that stores the 'label' widget. The label widget is created
using the 'tkinter' label class. The root part of this line
makes this this label a child of the 'root' window. It 
essentially makes the label INSIDE the main window. The 'text'
part of this line sets the text that is to be diaplayed and in
this case it is 'Score:__' where the value of score is a 
placeholder for the actual score that will be updated as the
game progresses. The 'font' part of this line sets the font
style as well as the size of the font. 

The seventh line of this code displays the label in the window.
The 'pack()' is a geometry manager method, and it tells tkinter
to show this widget in the parent window using the pack layout.
Without this line, the label exists in memory but is invisible.

The eighth line of this code block creates a canvas variable that
stores a Canvas widget using tkinter's Canvas class. This 
variable makes the canvas a child of the 'root' window. the bg 
part of this code sets the background to the constant 
'BACKGROUND_COLOR', the height part of this line is set to the
constant 'GAME_HEIGHT', and the width part is set to the 
constant 'GAME_WIDTH'. This line creates a 700x700 dark blue
drawing area inside the main window where the game will be played.

The next line is 'canvas.pack()'. This line displays the canvas
in the window. Similar to the 'label.pack()' line, this line
uses the pack geometry manager to show the canvas widget. It 
positions the canvas below the score label. Without this line,
the canvas exists, but it is invisible.

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

"""
This block of code is responsible to prefectly center the game
window on the user's screen. Without this code the window will
appear at the top0left corner (0,0), but becuase it is present
the code will appear perfectly centered in the middle of the 
screen. 

The first line of code in this block calls the 'update()' method
of the 'root' window. This method forces tkinter to immediately
update/draw the window. This line refreshes the window and 
processes all pending GUI events. It makes sure widgets are 
fully rendered before continuing. Without this line of code,
the next lines might get wrong or the measurements might be
old. This is basically like presentung the 'refresh' button
to get the latest updates on the window.

The second and third line of code in this block assign the
window's actual width and height to the variables 'root_width'
and 'root_height' respectively. The 'winfo_width()' and the 
'winfo_height()' methods of the 'root' window are used to get
the real-time measurements of the width. These measure the game 
window, which in this case is 700x700 + title bar.

The fourth and fifth line of this block assigns the user's
full screen width and height to the variables 'screen_width'
and 'screen_height' respectively. The 'winfo_screenwidth()' and
'winfo_screenheight()' methods of the 'root' window are used to
get the real-time measurements of the user's screen. These
measure the user's full screen, which can be different for each
user. For example, one user might have a 1920x1080 screen, while
another user might have a 2560x1440 screen.
"""
root.update()
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

"""
This block of code centers the window on screen and initializes
the game objects. 
Lines one and two are calculate are variables x and y, that
are hold the integer value of the x and y coordinates for the
exact pixcel position to center the window.

Line 3 is used to apply the window position. It moves the 
window into the centered position.

Line 4 is used to create the Snake game object. The purpose 
of this is to prepare the snake for the game.

Line 5 creates the Food game object. It creates a representative
of the 'Food' class. It stores the class in the 'food'
variable. It prepares the food for the game.
"""
x = int((screen_width/2) - (root_width/2))
y = int((screen_height/2) - (root_height/2))

root.geometry(f"{root_width}x{root_height}+{x}+{y}")

snake = Snake()
food = Food()


root.mainloop()

