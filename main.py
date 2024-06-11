# Importing the Pygame Zero Library
import pgzrun
from random import randint

# Title for game window
TITLE = "Good Shot"
# width and height of game window
WIDTH = 800
HEIGHT = 800

# variable to store the message displayed on the screen
msg = ""


alien = Actor('alien')



#function for updating the screen
def draw():
 
  screen.clear()
  screen.fill(color = "#F9DC5C")

  alien.draw()
  screen.draw.text(msg, center = (400, 30), fontsize= 40, color = "black")

def place_alien():
  alien.x = randint(50, WIDTH-50)
  alien.y = randint(50, WIDTH-50)

def on_mouse_down(pos):
 
  global msg
  if alien.collidepoint(pos):
    msg = "Good Shot"
    place_alien()
  else:
    msg = "You missed"

# method to start running the game
place_alien()
pgzrun.go()