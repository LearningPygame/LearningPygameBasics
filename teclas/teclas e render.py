import pygame
pygame.init()
window=pygame.display.set_mode ((800,600))

black = (0,0,0)
white= (255,255,255)


clock =pygame.time.Clock()

class Sprite:
    def _init_(self,x,y):
        self.x=x
        self.y=y
        self.width=50
        self.height=50
    def render(self):
        pygame.draw.rect(window,white,(self.x,self.y,self.width,self.height))

player = Sprite(50,100)

gameLoop=True
while gameLoop:
    for event in pygame.event.get():
        if(event.type==pygame.QUIT):
            gameLoop=False
        if(event.type==pygame.KEYDOWN):
            if(event.key==pygame.K_LEFT):
                moveX = -5
            if(event.key==pygame.K_RIGHT):
                moveX = 5
            if(event.key==pygame.K_UP):
                moveY = -5
            if(event.key==pygame.K_DOWN):
                moveY = 5
        if(event.type==pygame.KEYUP):
            if(event.key==pygame.K_LEFT):
                moveX = 0
            if(event.key==pygame.K_RIGHT):
                moveX = 0
            if(event.key==pygame.K_UP):
                moveY = 0
            if(event.key==pygame.K_DOWN):
                moveY = 0

    window.fill(black)

    player.x+=moveX
    player.y+=moveY

    player.render()
    
    clock.tick(30)
    pygame.display.flip()
pygame.quit()
                     
