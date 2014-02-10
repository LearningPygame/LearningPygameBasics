import pygame

pygame.init()

screenDimensions = (800,600)

window = pygame.display.set_mode(screenDimensions, pygame.RESIZABLE)
image = pygame.image.load("bg.jpg")
running = True

while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	
	window.blit(image, (100,300))
	
	pygame.display.update()

pygame.quit()