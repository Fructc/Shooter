from pygame import*

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image=transform.scale(image.load(player_image),(65,65))
        self.speed=player_speed
        self.rect=self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update(self):
        kyes+eky.get_pressed()
        if kyes[K_LEFT] and  self.rect.x > 5:
            self.rect.x -=self.speed
        if kyes[K_RIGHT] and  self.rect.x < win_width - 65:
            self.rect.y +=self.speed
        if kyes[K_UP] and  self.rect.y > 5:
            self.rect.y -=self.speed
        if kyes[K_LEFT] and  self.rect.y < win_height - 65:
            self.rect.y +=self.speed

class Enemy(GameSprite):
    direction='left'
    def update(self):
        if self.rect.x <= 470:
            self.direction ='right'
        if self.rect.x >= win_width - 85:
            self.direction ='left'

        if self.direction=='left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

win_width=700
win_height=500
window=display.set_mode((win_width,win_height))
display.set_caption('Cиберпуке9999')
background=transform.scale(image.load('background.jpg'),(win_width,win_height))

player=PLayer('hero.png',5,win_height-80, 4)
monster=Enemy('cyborg.png',win_width-80,280,2)
final=GameSprite('treasure.png',win_width-120,win_height-80,0)

game=True
clock=time.Clock()
FPS=60

mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.set_volume(0.5)
mixer.music.play()

finish=False

while game:
    for e in event.get():
        if e.type==QUIT:
            game=false

    if finish != True:
        window.blit(background,(0,0))

        player.update()
        monster.update()
        
        player.reset()
        monster.reset()
        final.reset()
        display.update()
        clock.tick(FPS)

