import pygame
import os
import random


# GEOMETRY

WIDTH = 350
HEIGHT = 450
FPS = 60 #Frame Rate per second

# COLOR

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
SEA = (159, 192, 245)

#Initialize Pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

######CREATE SUBMARINE#######
#game_folder = os.path.dirname(__file__)
# game_folder C:\Users\Uncle Engineer\Desktop\Python Pygame
#img_folder = os.path.join(game_folder, 'img')

# img_folder C:\Users\Uncle Engineer\Desktop\Python Pygame\img
#print(game_folder)

class Player(pygame.sprite.Sprite):

	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		#sub_img = os.path.join(img_folder,'D:/per/compro/game/player.png')

		self.image = pygame.image.load('D:/per/compro/game/player.png')
		#self.image.set_colorkey(BLACK)
		#self.image.fill(BLUE)
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

class Enemy

# sprite is a player
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

enemys = pygame.sprite.Group()
for i in range(10):
    em = Enemy()
    all_sprites.add(em)
    enemys.add(em)
    

running = True

while running:
	clock.tick(FPS)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	all_sprites.update()

	screen.fill(WHITE)
	all_sprites.draw(screen)
	pygame.display.flip()

pygame.quit()
