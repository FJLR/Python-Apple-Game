import pgzrun
from random import randint
apple = Actor('apple.png')
orange = Actor('orange.png')


def draw():
    screen.clear()
    #screen.blit('apple.png', (10, 10))
    apple.draw()
    orange.draw()
    
def place_apple():
    apple.x = randint(10, 800)
    
    
    apple.y = randint(10, 600)
    

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print("Good Shot Francisco...!")
        place_apple()
       
    else:
        print("...oops, you miss it")
        quit()
    
place_apple()


pgzrun.go()
#my first Python game develop on Oct. 17, 2021 - Tutor: Matt Szal.