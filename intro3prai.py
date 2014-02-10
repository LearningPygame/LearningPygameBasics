import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

window = pygame.display.set_mode((640,480))
pygame.display.set_caption("teste teste")

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
mousex, mousey = 0, 0

image = pygame.image.load("ball.png")
font = pygame.font.Font("freesansbold.ttf", 10)
msg = "Sup"

while True:
	window.fill(white)
	
	pygame.draw.circle(window, blue, (300,50), 20,0)
	pygame.draw.rect (window, red, (10,10,50,100))
	
	pixArr = pygame.PixelArray(window)
	for x in range (100,200,4):
		for y in range (100,200,4):
			pixArr[x][y] = red
	del pixArr
	
	window.blit(image, (mousex, mousey))
	
	msgimage = font.render(msg, False, blue)
	msgrectobj = msgimage.get_rect()
	msgrectobj.topleft = (10,20)
	window.blit(msgimage,msgrectobj)
	
	for event in pygame.event.get():
		if event.type == QUIT:
			 pygame.quit()
			 sys.exit()
			 
	pygame.display.update()
	clock.tick(30)
	
pygame.exit()
	
