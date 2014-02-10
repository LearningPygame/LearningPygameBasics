import pygame, sys, pygame.mixer
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)

w = 640
h = 480
z = 0

sound = pygame.mixer.Sound("bebe.wav")
bgFile = "background.jpg"
imageFile2 = "miranda2.jpg"
imageFile = "miranda.jpg"
bg = pygame.image.load(bgFile)
image = pygame.image.load(imageFile)
image2 = pygame.image.load(imageFile2)
window = pygame.display.set_mode((w,h))
pygame.display.set_caption("Eu chupo blocas o dia todo")

class Image:
	def __init__ (self, radius, x, y, color, size, maxforce, force, life):
		self.y=y
		self.x=x
		self.color=image
		self.size=(94, 96)
		self.maxforce=maxforce
		self.force=force
		self.radius=100
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
			window.blit(image2, (self.x,self.y))

ball = []
ball.append(Image(25, 250, 250, image, "L", 25, 1, 100))

gameLoop = True

while gameLoop:
	clock.tick(60)
	sound.play()
	x, y = pygame.mouse.get_pos()
	window.blit(bg, (0,0))
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
	

	for i in ball:
		i.fall()

	pygame.display.update()

