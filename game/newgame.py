import pygame
import random
import time

pygame.init()

clock = pygame.time.Clock()


width = 600
height = 400
display_surface = pygame.display.set_mode((600,400))

#last_score = []
#with open('D:/per/compro/game/score.csv','r')as f:
    #for i in f:
      #  last_score.append(int(i))



bg_img = pygame.image.load('D:/per/compro/game/na1.jpg')
target_img = pygame.image.load('D:/per/compro/game/object.png')
crosshair_img = pygame.image.load('D:/per/compro/game/tank.png')
sound = pygame.mixer.

pygame.mouse.set_visible(False)


def score_board(score):
    font = pygame.font.Font(None,40)
    text = font.render('Killed: ' + str(score),True,(0,0,0))
    display_surface.blit(text,(6,10))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = crosshair_img
        self.rect = self.image.get_rect()
        
    def update(self):
        self.rect.center = pygame.mouse.get_pos()

class Target(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = target_img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0,width-self.rect.width)
        self.rect.y = random.randint(-100,-40)        
        self.speedy = random.randrange(1,5)
        self.speedx = random.randrange(-1,1)

    def update(self):
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        
        #check
        if self.rect.right < 0 or self.rect.left > width:
            self.rect.x = random.randint(0,width-self.rect.width)
            self.rect.y = random.randint(-100,-40)
            self.speedy = random.randint(1,5)
            self.speedx = random.randint(-1,1)
            
        if self.rect.top > height:
            font = pygame.font.Font(None,80)
            text = font.render('Game Over',True,(0,0,0))
            display_surface.blit(text,(150,180))
            pygame.display.flip()
            time.sleep(20)
            game_loop()
            


def game_loop():
    
    #Player
    player = Player() 
    player_group = pygame.sprite.Group()
    player_group.add(player)

    #Target
    target_group = pygame.sprite.Group()
    for target in range(6):
        new_target = Target()
        target_group.add(new_target)

    score = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               quit()
               
            if event.type == pygame.MOUSEBUTTONDOWN: 
                hits = pygame.sprite.spritecollide(player,target_group,True)
                for hit in hits:
                    score = score + 1
                    new_target = Target()
                    target_group.add(new_target)

        display_surface.blit(bg_img,(0,0))

        target_group.update()   
        target_group.draw(display_surface)

        player_group.update()
        player_group.draw(display_surface)

        score_board(score)

        pygame.display.flip()
        clock.tick(60)


game_loop()
pygame.quit()
quit()