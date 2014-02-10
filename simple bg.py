bif="bg.jpg"

import pygame, sys
import pygame.locals import *

pygame.init()
screen=pygame.display.set_mode((275, 183),0,32)

background=pygame.image.load(bif).convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0,0))

    pygame.display.update()
    
