import random
import pygame
import sys
pygame.init()
screen_width=400
screen_height=700
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load('./img/background.png')
plane=pygame.image.load('./img/plane.png').convert_alpha()
ball=pygame.image.load('./img/ball.png')
enemy1=pygame.image.load('./img/enemy1.png')
enemy2=pygame.image.load('./img/enemy2.png')
font=pygame.font.Font('./simkai.ttf',25)
game_music=pygame.mixer.Sound('./audio/game_music.mp3')
ball_shoot=pygame.mixer.Sound('./audio/ball.mp3')
enemy_down=pygame.mixer.Sound('./audio/ball.mp3')
FPS=60
clock=pygame.time.Clock()
class Plane(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = plane
        self.rect = self.image.get_rect()
        self.rect.centerx=200
        self.rect.bottom=screen_height-10
    def move(self):
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.rect.x-=5
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.rect.x+=5
        if self.rect.x<0:
            self.rect.x=0
        if self.rect.x>screen_width-self.rect.width:
            self.rect.x=screen_width-self.rect.width
        return self.rect.centerx,self.rect.top

class Ball(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = ball
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = y
    def shoot(self):
        self.rect.y-=10
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = random.choice([enemy1,enemy2])
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0,screen_width-self.rect.width)
        self.rect.y = random.randrange(-100,-40)
        self.speed = random.randrange(2,5)
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > screen_height+10 :
            self.rect.x = random.randrange(0, screen_width - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speed = random.randrange(1, 3)
    def add(self):
        self.rect.x = random.randrange(0, screen_width - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        self.speed = random.randrange(1, 3)

play = Plane()
enemies=[]
for i in range(3):
    enemy=Enemy()
    enemies.append(enemy)
pygame.display.set_caption('飞机大战')
pygame.display.flip()
circles=[]
score=0
start=True
game_music.play()
while start:
    clock.tick(FPS)
    x, y = play.move()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                ball_shoot.play()
                circle = Ball(x, y)
                circles.append(circle)
    for b in circles:
        b.rect.y-=10
    for c in enemies:
        c.update()
    for b in circles:
        for e in enemies:
            if b.rect.colliderect(e.rect):
                enemy_down.play()
                enemies.remove(e)
                circles.remove(b)
                score+=10
    if len(enemies)<2:
        for i in range(2):
            enemy = Enemy()
            enemies.append(enemy)
    text=font.render(f'{score}',True,(255,0,0))
    text_width, text_height = text.get_size()
    for e in enemies:
        if play.rect.colliderect(e.rect):
            start=False
    screen.blit(background,(0,0))
    screen.blit(plane,play.rect)
    for b in circles:
        screen.blit(ball,b.rect)
    for c in enemies:
        screen.blit(c.image,c.rect)
    screen.blit(text,((screen_width-text_width)//2,10))
    pygame.display.update()
