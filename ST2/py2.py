import pygame, sys
from pygame.locals import *

pygame.init()
clock = pygame.time.Clock()

white = (255,255,255)
black = (0,0,0)

w = 640
h = 480
z = 0

window = pygame.display.set_mode((w,h))
pygame.display.set_caption("This is nice")

class Ball:
	def __init__(self, radius, x, y, color, size, maxforce, force, life):
		self.y=y
		self.x=x
		self.size=size
		self.maxforce=maxforce
		self.force=force
		self.radius=radius
		self.color=color
		self.life=life
		pygame.draw.circle(window, self.color, (self.x, self.y), self.radius)

	def fall(self):
		if self.y < h-self.radius:
			self.y += self.force
			if self.force <self.maxforce:
				self.force += 1
		elif self.y > h-self.radius or self.y == h-self.radius:
			self.y = h-self.radius-1
			self.force = self.force*-1
			self.maxforce = self.maxforce/2
		pygame.draw.circle(window, self.color, (self.x,self.y), self.radius)
		self.life-=1
		if self.life < 0:
			ball.remove(self)

ball = []
ball.append(Ball(25, 250, 250, (white), "L", 25, 1, 100))			

gameLoop = True

while gameLoop:
	
	clock.tick(60)
	x,y = pygame.mouse.get_pos()
	
	for event in pygame.event.get():

		if(event.type == pygame.QUIT):
			gameLoop = False

		elif event.type == MOUSEBUTTONDOWN:
			z = 1
		elif event.type == MOUSEBUTTONUP:
			z = 0

	if z == 1:
		ball.append(Ball(25, x, y, (white), "L", 25, 1, 100))
		z = 3
	elif z > 1:
		z -= 1

	window.fill(black)

	for i in ball:
		i.fall()

	pygame.display.update()

pygame.exit()


