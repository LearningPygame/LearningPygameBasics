import pygame
from pygame import *

pygame.init()

black = (0,0,0)
white = (255,255,255)

screenDimensions =(800,600)
window = pygame.display.set_mode(screenDimensions, pygame.RESIZABLE)
image = pygame.image.load("bg.jpg")
gameLoop = True

while gameLoop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	window.fill(black)

	pygame.display.update()

pygame.quit()
