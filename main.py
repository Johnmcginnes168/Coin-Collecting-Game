####################################
#
#   Import Libraries
#
####################################
import os
import sys
from random import randint
import pgzrun

#Get the absolute path to the resource for dev and packaged executables.
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".") 
    
    return os.path.join(base_path, relative_path)

####################################
#
#   Initialize Variables and Actors
#
####################################
WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

#Load the icon image from the pgz_data folder
try:
    icon_path = resource_path("pgz_data/icon.png")
    pgzrun.set_icon(icon_path)
except Exception as e:
    print(f"Error loading icon: {e}")

fox = Actor(resource_path("images/fox.png"))
fox.pos = 100, 100

coin = Actor(resource_path("images/coin.png"))
coin.pos = 200, 200

hedgehog = Actor(resource_path("images/hedgehog.png"))
hedgehog.pos = 300, 300

####################################
#
#   Main Draw Function
#
####################################

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    hedgehog.draw()
    screen.draw.text(f"Score: {score}", color = "black", topleft = (10,10))

    if game_over:
        screen.fill("pink")
        screen.draw.text(f"Final Score: {score}", topleft = (10,10), fontsize = 60)
                     
####################################
#
#   Game Functions
#
####################################

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score

    # Fox Movement
    if keyboard.left:
        fox.x -= 2
    elif keyboard.right:
        fox.x += 2
    elif keyboard.up:
        fox.y -= 2
    elif keyboard.down:
        fox.y += 2

    # Hedgehog Movement
    if hedgehog.x < coin.x:
        hedgehog.x += 1
    elif hedgehog.x > coin.x:
        hedgehog.x -= 1
    if hedgehog.y < coin.y:
        hedgehog.y += 1
    elif hedgehog.y > coin.y:
        hedgehog.y -= 1

    #Coin Collection Logic  
    if fox.colliderect(coin):
        score += 10
        place_coin()
    elif hedgehog.colliderect(coin):
        place_coin()

clock.schedule(time_up, 30.0)
place_coin()
pgzrun.go()
