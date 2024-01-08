import pygame
import os
import random
import time



WIDTH = 350
HEIGHT = 550
FPS = 60 

score = 0


image = pygame.image.load('D:/per/compro/game/sky.jpg')
image = pygame.transform.scale(image, (600, 600))
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#csv
#last_score = []
#with open('score.csv','r')as f:
	#for    #for i in f:
      #  last_score.append(int(i))


def score_board(score):
    font = pygame.font.Font(None,30)
    text = font.render('Point ' + str(score),True,(0,0,0))
    screen.blit(text,(5,10))



class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('D:/per/compro/game/pom1.png')
		self.rect = self.image.get_rect()
		self.rect.centerx = WIDTH / 2
		self.rect.bottom = HEIGHT - 30

		self.speedx = 0

	def update(self):
		self.speedx = 0
		keystate = pygame.key.get_pressed()
		if keystate[pygame.K_LEFT]:
			self.speedx = -5

		if keystate[pygame.K_RIGHT]:
			self.speedx = 5

		self.rect.x += self.speedx

		if self.rect.right > WIDTH:
			self.rect.right = WIDTH

		if self.rect.left < 0:
			self.rect.left = 0

		print(self.rect.centerx)


class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('D:/per/compro/game/clock.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speedy = random.randrange(1,5)

    def update(self):
        self.rect.y = self.rect.y + self.speedy
        
        #check
        if self.rect.right < 0 or self.rect.left > WIDTH:
            self.rect.x = random.randint(0,WIDTH-self.rect.width)
            self.rect.y = random.randint(-100,-40)
            self.speedy = random.randint(1,2)
            self.speedx = random.randint(-1,1)
            
        if self.rect.top > HEIGHT:
            font = pygame.font.Font(None,40)
            text = font.render('Game Over',True,(0,0,0))
            screen.blit(text,(105,255))
            pygame.display.flip()
            time.sleep(10)
            
	


       

    

    
        


all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

enemy = pygame.sprite.Group()
for i in range(10):
	em = Enemy()
	all_sprites.add(em)
	enemy.add(em)
	
    
    

running = True

while running:
	clock.tick(FPS)
	screen.blit(image,(0,0))
	score_board(score)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	all_sprites.update()

	hits = pygame.sprite.spritecollide(player,enemy,True)
	for hit in hits:
		score = score+1
		em = Enemy()
		all_sprites.add(em)
		enemy.add(em)
	

	all_sprites.draw(screen)
	pygame.display.flip()
	
	
	 



		
pygame.quit()