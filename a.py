import pygame
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(player_image),(size_x, size_y))
        self.rect = self.image.get_rect()
        self.rect.x=player_x
        self.rect.y=player_y


    def reset(self):
        win.blit(self.image,(self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y,player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.x_speed=player_x_speed
        self.y_speed=player_y_speed

    def update(self):
        if hero.rect.x <= win_width-80 and hero.x_speed > 0 or hero.rect.x >= 0 and hero.x_speed <0:
            self.rect.x += self.x_speed
        platforms_touched=sprite.spritecollide(self,spr_next,False)
        if self.x_speed>0:
            for p in platforms_touched:
                self.rect.right=min(self.rect.right, p.rect.left)
        elif self.x_speed<0:
            for p in platforms_touched:
                self.rect.left=max(self.rect.left, p.rect.right)
        if hero.rect.y <= win_height-80 and hero.y_speed > 0 or hero.rect.y >= 0 and hero.y_speed <0:
            self.rect.y += self.y_speed
        platforms_touched=sprite.spritecollide(self,spr_next,False)
        if self.y_speed >0:
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
                self.rect.bottom=min(self.rect.bottom,p.rect.top)    
        elif self.y_speed < 0:
            for p in platforms_touched:
                self.rect.top=max(self.rect.top, p.rect.bottom)

    def fire(self):
        bullet=Bullet('pictures/kknife.png',self.rect.centerx,self.rect.top,15,20,15)
        bullets.add(bullet)

class Enemy(GameSprite):
    side = 'left'
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed, start_x1, start_x2): 
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)        
        self.speed=player_speed
        self.start_x1=start_x1
        self.start_x2=start_x2
        
    def update(self):
        if self.rect.x <= self.start_x1: 
            self.side='right'
        if self.rect.x >= win_width - self.start_x2: 
            self.side='left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

        


class Button(GameSprite):
    def __init__(self, picture, w, h, x, y):
        GameSprite.__init__(self, picture, w, h, x, y)
        self.x = x
        self.y = y

    def colidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

class Bullet(GameSprite):
    def __init__(self,player_image,player_x,player_y,size_x,size_y,player_speed):
        GameSprite.__init__(self,player_image,player_x,player_y,size_x,size_y)
        self.speed=player_speed

    def update(self):
        self.rect.x +=self.speed
        if self.rect.x > win_width+10:
            self.kill()

def menu():
    global back,clock,play,play_btn,exit,exit_btn,FPS
    back=transform.scale(image.load('fon/first_screen.jpg'), (1000, 650))  
    clock = pygame.time.Clock()
    FPS = 30

    play= pygame.image.load('pictures/sttart.png')
    exit = pygame.image.load('pictures/exit.png')

    play_btn = Button(play, (128, 64), 430, 400)
    exit_btn  = Button(exit, (45,42), 950, 10)


SIZE = WIDTH , HEIGHT= 1000, 650
win_width=1000
win_height=650
pygame.init()
win = display.set_mode((win_width,win_height))
pygame.display.set_caption('Cave')


hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)
mixer.init()
mixer.music.load('music/song.mp3')
mixer.music.play(-1)
monster=sprite.Group()
bullets=sprite.Group()
spr_next=sprite.Group()
nevidimka_level_1=GameSprite('pictures/Colide.jpg',50,10,540,899)
nevidimka_level_2 = GameSprite('pictures/Colide.jpg',50,10,540,0)


def ffirst():
    one=image.load('fon/fonn8.jpg')

    nextt = GameSprite('pictures/strelk2.png', 0,430,80,80)

    enemy1=Enemy('pictures/enemy_brrr.png',300,430,150,150,5, 100, 600)
    win.blit(transform.scale(one,(win_width,win_height)),(0,0))
    monster.add(enemy1)
    spr_next.add(nextt)
    nextt.reset()
    hero.reset()
    hero.update()
    bullets.update()
    bullets.draw(win)


def ssecond():
    global listt
    two=image.load('fon/fonn1.jpg')
    nextt1 = GameSprite('pictures/strelk.png', 900,500,80,80)
    nextt2 = GameSprite('pictures/strelk2.png', 0,500,80,80)
    enemy2=Enemy('pictures/enemy_brrr.png',700,490,150,150,10, 600, 200)
    listt=GameSprite('pictures/spysook.png', 320,520,80,80)

    win.blit(transform.scale(two,(win_width,win_height)),(0,0))
    monster.add(enemy2)
    spr_next.add(nextt1)
    spr_next.add(nextt2)
    listt.reset()
    hero.reset()
    hero.update()
    nextt1.reset()
    nextt2.reset()
    bullets.update()
    bullets.draw(win)

def tthird():
    
    three=image.load('fon/fonn2.jpg')


    nextt3 = GameSprite('pictures/strelk.png', 900,500,80,80)
    nextt33 = GameSprite('pictures/strelk2.png', 0,500,80,80)
    enemy3=Enemy('pictures/enemy_brrr.png',700,490,150,150,15, 450, 200)
    win.blit(transform.scale(three,(win_width,win_height)),(0,0))
    monster.add(enemy3)
    spr_next.add(nextt3)
    spr_next.add(nextt33)
    nextt3.reset()
    nextt33.reset()
    hero.reset()
    hero.update()
    bullets.update()
    bullets.draw(win)
def ffourth():
    global listt1
    four=image.load('fon/fonn3.jpg')
    nextt4 = GameSprite('pictures/strelk.png', 900,500,80,80)
    nextt5 = GameSprite('pictures/strelk2.png', 0,500,80,80)
    enemy4=Enemy('pictures/enemy_brrr.png',700,450,150,150,15, 300, 200)
    listt1=GameSprite('pictures/spysook.png', 700,510,80,80)
    win.blit(transform.scale(four,(win_width,win_height)),(0,0))
    monster.add(enemy4)
    spr_next.add(nextt4)
    spr_next.add(nextt5)
    nextt4.reset()
    nextt5.reset()
    listt1.reset()
    hero.reset()
    hero.update()
    bullets.update()
    bullets.draw(win)

def ffifth():
    global listt2, listt3
    five=image.load('fon/fonn5.jpg')




    enemy5=Enemy('pictures/zub.png',700,380,150,150,15, 500, 200)
    enemy6=Enemy('pictures/zub.png',700,380,150,150,15, 500, 200)
    enemy7=Enemy('pictures/zub.png',700,380,150,150,15, 200, 500)
    enemy8=Enemy('pictures/zub.png',700,380,150,150,15, 200, 500)
    nextt6 = GameSprite('pictures/strelk.png', 900,400,80,80)
    nextt7 = GameSprite('pictures/strelk2.png', 0,400,80,80)

    
    listt3=GameSprite('pictures/spysook.png', 700,390,80,80)
    listt2=GameSprite('pictures/spysook.png', 300,390,80,80)
    win.blit(transform.scale(five,(win_width,win_height)),(0,0))
    monster.add(enemy5)
    monster.add(enemy6)
    monster.add(enemy7)
    monster.add(enemy8)
    spr_next.add(nextt6)
    spr_next.add(nextt7)
    nextt6.reset()
    nextt7.reset()
    listt2.reset()
    listt3.reset()
    bullets.update()
    bullets.draw(win)
    hero.reset()
    hero.update()
def ssixth():
    global listt4
    six=image.load('fon/end.jpg')



    enemy9=Enemy('pictures/gizmo.png',100,450,250,200,30, 100, 450)
    enemy10=Enemy('pictures/gizmo.png',100,450,250,200,30, 100, 490)
    enemy11=Enemy('pictures/gizmo.png',100,450,250,200,30, 100, 600)
    enemy12=Enemy('pictures/gizmo.png',100,450,250,200,30, 100, 550)
    nextt8 = GameSprite('pictures/strelk.png', 900,490,80,80)
    listt4=GameSprite('pictures/spysook.png', 250,430,80,80)
    win.blit(transform.scale(six,(win_width,win_height)),(0,0))
    monster.add(enemy9)
    monster.add(enemy10)
    monster.add(enemy11)
    monster.add(enemy12)
    spr_next.add(nextt8)
    bullets.update()
    bullets.draw(win)
    hero.reset()
    hero.update()
    nextt8.reset()
    listt4.reset()

amount=0
score = 0
start_menu=True
level_1 = True
level_2 = False
main_menu = True
game_over = False
level_won = False
escape = False
false=False
finish=False
run=True
while run:
    pressed_keys = pygame.key.get_pressed()
    for i in event.get():
        if i.type == QUIT:
            run = False
        elif i.type == KEYDOWN:
            if i.key== K_LEFT:
                hero.x_speed = -5
                #hero= Player('player/karoline_walkkk.png',5,win_height - 490,80,80,0,0)
            elif i.key== K_RIGHT:
                hero.x_speed = 5
                #hero= Player('player/karoline_walkk.png',5,win_height - 490,80,80,0,0)
            elif i.key == K_DOWN:
                hero.y_speed = 5
                #hero= Player('player/karoline_walkk.png',5,win_height - 490,80,80,0,0)
            elif i.key == K_UP:
                hero.y_speed = -5
                #hero= Player('player/karoline_walkk.png',5,win_height - 490,80,80,0,0)
            elif i.key== K_a:
                hero.x_speed = -5
                #hero= Player('player/karoline_walkkk.png',5,win_height - 490,80,80,0,0)
            elif i.key== K_d:
                hero.x_speed = 5  
                #hero= Player('player/karoline_walkk.png',5,win_height - 490,80,80,0,0) 
            elif i.key == K_w:
                hero.y_speed = -5
                #hero= Player('player/karoline_walkk.png',5,win_height - 490,80,80,0,0)
            elif i.key == K_s:
                hero.y_speed = 5
                #hero= Player('player/karoline_walkk.png',5,win_height - 490,80,80,0,0)
            elif i.key == K_SPACE:
                hero.fire()      
        elif i.type == KEYUP:
            if i.key== K_LEFT:
                hero.x_speed = 0
                #hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)
            elif i.key== K_RIGHT:
                hero.x_speed = 0
                #hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)
            elif i.key == K_UP:
                hero.y_speed = 0
                #hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)
            elif i.key == K_DOWN:
                hero.y_speed = 0
                #hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)
            if i.key== K_a:
                hero.x_speed = 0
                #hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)
            elif i.key== K_d:
                hero.x_speed = 0
                #hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)
            elif i.key == K_w:
                hero.y_speed = 0
                #hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)
            elif i.key == K_s:
                hero.y_speed = 0
                #hero= Player('player/karoline_staandd.png',5,win_height - 490,80,80,0,0)



    if start_menu:
            fon_start_menu = transform.scale(image.load("fon/first_screen.jpg"), [1000, 650])
            win.fill((255, 255, 255))
            win.blit(fon_start_menu, (0, 0))
            button_story = Button("pictures/sttart.png", 400, 400, 200, 80)
            button_story.reset()
            for i in event.get():
                if i.type == MOUSEBUTTONDOWN and i.button == 1:
                    x, y = i.pos
                    if button_story.colidepoint(x, y):
                        start_menu = False
                        level_1 = True

    if not finish:
        if level_1:
            if sprite.collide_rect(nevidimka_level_2, hero):
                level_1 = False
                level_2 = True
                hero.level_update(2)
        if level_2:
            if sprite.collide_rect(nevidimka_level_1, hero):
                level_2 = False
                level_1 = True
                hero.level_update(1)
        spr_next.update()
        spr_next.draw(win)
        sprite.groupcollide(monster,bullets, True,True)
        monster.update()
        monster.draw(win)
        sprite.groupcollide(bullets,spr_next,True,False)
        ffirst()
        ssecond()
        tthird()
        ffourth()
        ffifth()
        ssixth()
        if not false:
            if sprite.collide_rect(hero,listt):
                false=True
                amount+=1
                del listt
            if sprite.collide_rect(hero,listt2):
                false=True
                amount+=1
                del listt2
            if sprite.collide_rect(hero,listt1):
                false=True
                amount+=1
                del listt1
            if sprite.collide_rect(hero,listt3):
                false=True
                amount+=1
                del listt3
            if sprite.collide_rect(hero,listt4):
                false=True
                amount+=1
                del listt4
        if sprite.spritecollide(hero,monster,False):
            finish=True
            img=image.load('fon/game__over.jpg')
            win.blit(transform.scale(img,(win_width,win_height)),(0,0))
        if sprite.collide_rect(hero,listt) and amount == 5:
            if false==True:
                finish=True
                img=image.load('fon/you__win.jpg')             
                win.blit(transform.scale(img,(win_width,win_height)),(0,0))

    

    time.delay(2)
    display.update()
