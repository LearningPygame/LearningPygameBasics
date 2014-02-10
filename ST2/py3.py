import pygame, sys
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)

w = 640
h = 480
z = 0

imageFile = "bg.jpg"
image = pygame.image.load(imageFile)
window = pygame.display.set_mode((w,h), RESIZABLE)
pygame.display.set_caption("Nice")

class Image:
	def __init__ (self, radius, x, y, color, size, maxforce, force, life):
		self.y=y
		self.x=x
		self.color=image
		self.size=(275, 183)
		self.maxforce=maxforce
		self.force=force
		self.radius=183
		self.life=life
                
		window.blit(image, (self.x,self.y))

	def fall (self):
		if self.y < h-self.radius:
			self.y += self.force
			if self.force < self.maxforce:
				self.force += 1

		elif self.y > h-self.radius:
			self.y = h-self.radius - 1
			self.force = self.force *-1
			self.maxforce = self.maxforce/2

		window.blit(image, (self.x,self.y))
		self.life -= 1
		if self.life < 0:
			ball.remove(self)

ball = []
ball.append(Image(25, 250, 250, image, "L", 25, 1, 100))

gameLoop = True

while gameLoop:
	clock.tick(60)
	x, y = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
			pygame.quit()
		elif event.type == MOUSEBUTTONDOWN:
			z = 1
		elif event.type == MOUSEBUTTONUP:
			z = 0

	if z == 1:
		ball.append(Image(25, x, y, image, "L", 25, 1, 100))	
		z = 3
	elif z > 1:
		z -= 1
	window.fill(black)

	for i in ball:
		i.fall()

	pygame.display.update()

