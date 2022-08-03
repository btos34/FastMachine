
import pygame
import subprocess
import sys
import random

RandCaption = random.randint(1,3)

def copy2clip(txt):
    cmd='echo '+txt.strip()+'|clip'
    return subprocess.check_call(cmd, shell=True)
copy2clip("sarue was here")




## Configeration

## colors
WHITE = (200,200,200)
BLACK = (0,0,0)
GREY = (50,50,50)

pygame.init()
font = pygame.font.SysFont('Arial', 20)
objects = []

# random title from flash script
if RandCaption == 1:
    pygame.display.set_caption("FastMachine: To understand what I'm about to tell you, you need to do something first.")
if RandCaption == 2:
    pygame.display.set_caption("FastMachine: You need to believe in the impossible. Can you do that? Good.")
else:
    pygame.display.set_caption("FastMachine: You see that red blur? That's me. That too. There I am again.")


 
pygame.init()
 
 


# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)
programIcon = pygame.image.load('resources/images/favicon.png')
screen.fill(GREY)

pygame.display.set_icon(programIcon)

def drawGrid():
    blockSize = 20 #Set the size of the grid block
    for x in range(0, 700, blockSize):
        for y in range(0, 500, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, WHITE, rect, 1)
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    drawGrid()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


