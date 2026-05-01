"""
The 2 import statements import python libraries that are used
in this code.
The 'import tkinter as tk' imports Python's built-in library
for the GUI library 'tkinter'. This line imports the built-in
library as tk so the prefix 'tk.' is used to access the functions
and classes from the tkinter library. This imported library lets
you create windows, buttons, labels, etc.
The 'import random' imports Python's built-in random library
that is typically used to generate random numbers.
"""
import tkinter as tk
import random

"""
The 8 variables that are defined here are constants. These are
values that are not to be changed and are kind of like the
game's settings. 
GAME_WIDTH = 700: Window width in pixels
GAME_HEIGHT = 700: Window height in pixels  
SPEED = 100: Speed of the snake (lower = faster)
SPACE_SIZE = 50: Size of game items in pixels
BODY_PARTS = 3: Number of body parts at beginning
SNAKE_COLOR = "#46E28C": Color of snake body
FOOD_COLOR = "red": Color of food that snake eats
BACKGROUND_COLOR = "#00025B": Color of background in game
"""
GAME_WIDTH = 700  # Window width in pixels
GAME_HEIGHT = 700  # Window height in pixels
SPEED = 100  # Speed of the snake
SPACE_SIZE = 50  # Size of game items in pixels
BODY_PARTS = 3  # Number of body parts in beginning
SNAKE_COLOR = "#46E28C"  # Color of snake body
FOOD_COLOR = "#DE5983"  # Color of food that snake eats
BACKGROUND_COLOR = "#00013C"  # Color of background in game

class Snake:
    """
    This class creates a 3-segment snake at position (0, 0) on the canvas.
    """
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            oval = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, 
                                    fill=SNAKE_COLOR, tag="snake")
            self.squares.append(oval)

class Food:
    """
    This class creates food at a random position on the canvas.
    """
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]

        self.square = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, 
                                       fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    oval = canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, 
                            fill=SNAKE_COLOR, tag="snake")
    snake.squares.insert(0, oval)

    del snake.coordinates[-1]

    if x == food.coordinates:
        pass

    canvas.delete(snake.squares[-1])

    del snake.squares[-1]

    root.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction

    if new_direction == 'left' and direction != 'right':
        direction = new_direction
    elif new_direction == 'right' and direction != 'left':
        direction = new_direction
    elif new_direction == 'up' and direction != 'down':
        direction = new_direction
    elif new_direction == 'down' and direction != 'up':
        direction = new_direction

def check_collisions(snake, food):
    pass

def game_over():
    pass

# Create main application window
root = tk.Tk()
root.title("Snake Game")
root.resizable(False, False)

score = 0
direction = 'down'

label = tk.Label(root, text=f"Score: {score}", font=("Arial", 40))
label.pack()

canvas = tk.Canvas(root, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

# Center window on screen
root.update()
root_width = root.winfo_width()
root_height = root.winfo_height()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = int((screen_width / 2) - (root_width / 2))
y = int((screen_height / 2) - (root_height / 2))
root.geometry(f"{root_width}x{root_height}+{x}+{y}")

# Bind arrow keys to direction changes
root.bind('<Left>', lambda event: change_direction('left'))
root.bind('<Right>', lambda event: change_direction('right'))
root.bind('<Up>', lambda event: change_direction('up'))
root.bind('<Down>', lambda event: change_direction('down'))

# Initialize game objects
snake = Snake()
food = Food()

# Start game loop
next_turn(snake, food)
root.mainloop()
