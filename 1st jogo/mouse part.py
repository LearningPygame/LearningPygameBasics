import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("Mouse Part")
mousefile = "bg.jpg"
mouse = pygame.image.load(mousefile).convert_alpha()

while True:

    window.fill((255,255,255))
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    x,y = pygame.mouse.get_pos()

    x -= mouse.get_width()/2
    y -= mouse.get_height()/2

    window.blit(mouse, (x,y))
    
    pygame.display.update()
    clock.tick(30)

